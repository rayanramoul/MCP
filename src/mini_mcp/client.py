import streamlit as st
import json
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from litellm import experimental_mcp_client
import asyncio

# Load MCP server config
with open(os.path.expanduser("~/.cursor/mcp.json")) as f:
    mcp_config = json.load(f)["mcpServers"]

st.title("LiteLLM MCP Streamlit Demo")

# Server selection
server_names = list(mcp_config.keys())
server_choice = st.selectbox("Select MCP Server", server_names)
server_info = mcp_config[server_choice]

# Prepare server parameters
server_params = StdioServerParameters(
    command=server_info["command"],
    args=server_info["args"],
    env=server_info.get("env", None)
)

user_message = st.text_input("Enter a message for the LLM + tools:")

show_tools = st.button("Show Available MCP Tools")

if show_tools:
    async def show_mcp_tools():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")
                st.write("Available Tools:", tools)
    asyncio.run(show_mcp_tools())

if st.button("Send"):
    async def list_tools_and_respond(user_message):
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")
                # st.write("Available Tools:", tools)  # Only show if needed
                if user_message:
                    messages = [{"role": "user", "content": user_message}]
                    import litellm
                    llm_response = await litellm.acompletion(
                        model="gemini/gemini-2.0-flash-lite",
                        api_key=os.getenv("OPENAI_API_KEY"),
                        messages=messages,
                        tools=tools,
                    )
                    st.write("LLM Response:", llm_response)
    asyncio.run(list_tools_and_respond(user_message))

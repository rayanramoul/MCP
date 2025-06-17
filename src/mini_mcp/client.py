import streamlit as st
import json
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from litellm import experimental_mcp_client
import asyncio
import litellm

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
                    llm_response = await litellm.acompletion(
                        model="gemini/gemini-2.0-flash-lite",
                        api_key=os.getenv("OPENAI_API_KEY"),
                        messages=messages,
                        tools=tools,
                    )
                    st.write("LLM Response:", llm_response)

                    # 3. If the LLM wants to call a tool, call it
                    tool_calls = llm_response["choices"][0]["message"].get("tool_calls", [])
                    if tool_calls:
                        openai_tool = tool_calls[0]
                        call_result = await experimental_mcp_client.call_openai_tool(
                            session=session,
                            openai_tool=openai_tool,
                        )
                        st.write("MCP TOOL CALL RESULT: ", call_result)

                        # 4. Send the tool result back to the LLM
                        messages.append(llm_response["choices"][0]["message"])
                        messages.append(
                            {
                                "role": "tool",
                                "content": str(call_result),
                                "tool_call_id": openai_tool["id"],
                            }
                        )
                        st.write("final messages with tool result: ", messages)
                        llm_response = await litellm.acompletion(
                            model="gemini/gemini-2.0-flash-lite",
                            api_key=os.getenv("OPENAI_API_KEY"),
                            messages=messages,
                            tools=tools,
                        )
                        st.write(
                            "FINAL LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str)
                        )
                    else:
                        st.write("No tool call detected in LLM response.")
    asyncio.run(list_tools_and_respond(user_message))

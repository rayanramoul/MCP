launch_servers:
	uv run --no-sync src/mini_mcp/servers_launcher.py

run_client:
	uv run --no-sync streamlit run src/mini_mcp/client.py
from pathlib import Path
import libtmux
from typing import List


def get_server_files() -> List[Path]:
    """Get all Python server files from the servers directory."""
    servers_dir = Path(__file__).parent / "servers"
    return list(servers_dir.glob("*.py"))


def launch_servers() -> None:
    """Launch all servers in separate tmux windows."""
    # Initialize tmux server
    server = libtmux.Server()
    
    # Create or attach to session
    session_name = "mcp_servers"
    try:
        session = server.new_session(session_name=session_name, kill_session=True)
    except Exception as e:
        print(f"Error creating tmux session: {e}")
        return

    # Get server files
    server_files = get_server_files()
    
    # Create a window for each server
    for i, server_file in enumerate(server_files):
        server_name = server_file.stem
        command = f"uv run --no-sync mcp dev {server_file}"
        
        if i == 0:
            # Use the first window
            window = session.windows[0]
            window.rename_window(server_name)
            pane = window.panes[0]
        else:
            # Create new windows for subsequent servers
            window = session.new_window(window_name=server_name)
            pane = window.panes[0]
        
        # Send the command to the pane
        pane.send_keys(command, enter=True)


def main() -> None:
    """Main entry point."""
    launch_servers()


if __name__ == "__main__":
    main()

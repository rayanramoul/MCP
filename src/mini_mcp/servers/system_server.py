# This library is language agnostic and available
# in most popular programming languages
from typing import Optional
import os
from mcp.server.fastmcp import FastMCP
import platform
import subprocess
from typing import Any


# Initialize the server
mcp = FastMCP("System Server")

@mcp.tool()
def notify_training_done(training_id: str, main_metric: str, value: float) -> None:
    """Send a system notification when training is done with the main metric result.
    
    Args:
        training_id: The ID of the completed training run
        main_metric: The name of the main metric (e.g., 'accuracy')
        value: The value of the main metric
    """
    title = f"Training Complete: {training_id}"
    message = f"{main_metric.capitalize()}: {value}"
    system = platform.system()
    if system == "Linux":
        subprocess.run([
            "notify-send", title, message
        ], check=False)
    elif system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run([
            "osascript", "-e", script
        ], check=False)
    else:
        print(f"[NOTIFY] {title} - {message}")


def main() -> None:
    """Manual test entry point: send a test notification."""
    import argparse
    parser = argparse.ArgumentParser(description="System notifier for training completion.")
    parser.add_argument("--training_id", type=str, required=True, help="Training run ID")
    parser.add_argument("--main_metric", type=str, required=True, help="Main metric name")
    parser.add_argument("--value", type=float, required=True, help="Main metric value")
    args = parser.parse_args()
    notify_training_done(args.training_id, args.main_metric, args.value)


if __name__ == "__main__":
    main()

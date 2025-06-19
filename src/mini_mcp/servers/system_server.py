# This library is language agnostic and available
# in most popular programming languages
from mcp.server.fastmcp import FastMCP
import platform
import subprocess

# Import pync conditionally to avoid issues on non-macOS systems
if platform.system() == "Darwin":
    try:
        from pync import Notifier
    except ImportError:
        print("[WARNING] pync not installed. Please install it with: pip install pync")
        Notifier = None


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
        if Notifier is not None:
            try:
                Notifier.notify(
                    message,
                    title=title,
                    sound="Glass"  # Use system sound
                )
            except Exception as e:
                print(f"[ERROR] Failed to send notification: {str(e)}")
        else:
            print(f"[WARNING] pync not available. {title} - {message}")
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

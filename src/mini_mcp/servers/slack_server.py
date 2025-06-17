# This library is language agnostic and available
# in most popular programming languages
from typing import Optional
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from mcp.server.fastmcp import FastMCP


# Initialize the server
mcp = FastMCP("Slack Bot")

# Initialize Slack client
slack_token = os.environ.get("SLACK_BOT_TOKEN")
if not slack_token:
    raise ValueError("SLACK_BOT_TOKEN environment variable is required")

client = WebClient(token=slack_token)


@mcp.tool()
def send_private_message(user_id: str, message: str) -> str:
    """Send a private message to a specific Slack user.
    
    Args:
        user_id: The Slack user ID to send the message to
        message: The message content to send
        
    Returns:
        str: Status message indicating success or failure
        
    Raises:
        SlackApiError: If there's an error communicating with Slack
    """
    try:
        # Open a DM channel with the user
        response = client.conversations_open(users=[user_id])
        channel_id = response["channel"]["id"]
        
        # Send the message
        client.chat_postMessage(
            channel=channel_id,
            text=message,
            as_user=True
        )
        return f"Message sent successfully to user {user_id}"
    except SlackApiError as e:
        error_message = f"Error sending message: {str(e)}"
        return error_message


@mcp.tool()
def get_user_info(user_id: str) -> str:
    """Get information about a Slack user.
    
    Args:
        user_id: The Slack user ID to look up
        
    Returns:
        str: User information or error message
    """
    try:
        response = client.users_info(user=user_id)
        user = response["user"]
        return f"User: {user['real_name']} (@{user['name']})"
    except SlackApiError as e:
        return f"Error getting user info: {str(e)}"


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

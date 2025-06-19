"""GCP Server for file operations using MCP."""
import os
from cloudpathlib import CloudPath
from mcp.server.fastmcp import FastMCP


# Initialize the server
mcp = FastMCP("GCP File Operations")

# Initialize GCP credentials
gcp_credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
if not gcp_credentials:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable is required")


@mcp.tool()
def list_files(bucket_path: str) -> list[str]:
    """List all files in a GCP bucket directory.
    
    Args:
        bucket_path: The GCP bucket path (e.g., 'gs://my-bucket/path/to/dir/')
        
    Returns:
        List[str]: List of file paths in the directory
        
    Raises:
        ValueError: If the bucket path is invalid
    """
    try:
        cloud_path = CloudPath(bucket_path)
        if not cloud_path.exists():
            return []
            
        # List all files in the directory
        files = [str(f) for f in cloud_path.iterdir() if f.is_file()]
        return files
    except Exception as e:
        raise ValueError(f"Error listing files: {str(e)}")

@mcp.resource("gcp://{username}")
def get_bucket_name_from_username(username: str) -> str:
    """Get the bucket name from the username.
    
    Args:
        username: The username to get the bucket name from
        
    Returns:
        str: The bucket name
        
    Raises:
        ValueError: If the username is invalid
    """
    return f"gs://runs_{username}_mrna"


@mcp.tool()
def download_file(bucket_path: str, local_path: str | None = None) -> str:
    """Download a file from GCP bucket and return its content.
    
    Args:
        bucket_path: The GCP bucket path to the file (e.g., 'gs://my-bucket/path/to/file.txt')
        local_path: Optional local path to save the file. If not provided, only returns content.
        
    Returns:
        str: The content of the file
        
    Raises:
        ValueError: If the file doesn't exist or can't be downloaded
    """
    try:
        cloud_path = CloudPath(bucket_path)
        if not cloud_path.exists():
            raise ValueError(f"File not found: {bucket_path}")
            
        # Download to local path if specified
        if local_path:
            cloud_path.download_to(local_path)
            print(f"File downloaded to: {local_path}")
            
        # Read and return content
        content = cloud_path.read_text()
        print(f"File content:\n{content}")
        return content
    except Exception as e:
        raise ValueError(f"Error downloading file: {str(e)}")


@mcp.tool()
def upload_file(local_path: str, bucket_path: str) -> str:
    """Upload a file to GCP bucket.
    
    Args:
        local_path: Local path to the file to upload
        bucket_path: The GCP bucket path where to upload (e.g., 'gs://my-bucket/path/to/file.txt')
        
    Returns:
        str: Success message with the uploaded file path
        
    Raises:
        ValueError: If the local file doesn't exist or can't be uploaded
    """
    try:
        if not os.path.exists(local_path):
            raise ValueError(f"Local file not found: {local_path}")
            
        cloud_path = CloudPath(bucket_path)
        cloud_path.upload_from(local_path)
        
        return f"File uploaded successfully to: {bucket_path}"
    except Exception as e:
        raise ValueError(f"Error uploading file: {str(e)}")


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

"""AI Server for simulating LLM training and generating reports."""
import random
import time
import json
from datetime import datetime
from typing import Dict, Optional
from dataclasses import dataclass
from mcp.server.fastmcp import FastMCP


# Initialize the server
mcp = FastMCP("AI Training Server")

# Store fake training runs
training_runs: Dict[str, Dict] = {}


@dataclass
class TrainingConfig:
    """Configuration for LLM training."""
    model_name: str = "gpt-3.5-turbo"
    learning_rate: float = 1e-4
    batch_size: int | float = 32
    num_epochs: int | float = 10
    max_seq_length: int | float = 2048
    warmup_steps: int | float = 1000
    weight_decay: float | int = 0.01
    gradient_accumulation_steps: int | float = 4
    fp16: bool | int = True
    num_train_samples: int | float = 1000000


@mcp.tool()
def launch_training(
    model_name: Optional[str] = None,
    learning_rate: None | float | int = None,
    batch_size: None | int | float = None,
    num_epochs: None | int | float = None,
    max_seq_length: None | int | float = None,
    warmup_steps: None | int | float = None,
    weight_decay: None | float | int = None,
    gradient_accumulation_steps: None | int | float = None,
    fp16: None | bool | int = None,
    num_train_samples: None | int | float = None,
) -> str:
    """Launch a fake LLM training run with the specified hyperparameters.
    
    Args:
        model_name: Name of the model to train
        learning_rate: Learning rate for optimization
        batch_size: Batch size for training
        num_epochs: Number of training epochs
        max_seq_length: Maximum sequence length
        warmup_steps: Number of warmup steps
        weight_decay: Weight decay for regularization
        gradient_accumulation_steps: Number of gradient accumulation steps
        fp16: Whether to use mixed precision training
        num_train_samples: Number of training samples
        
    Returns:
        str: Training run ID and status
    """
    # Create config with defaults and override with provided values
    config = TrainingConfig()
    if model_name:
        config.model_name = model_name
    if learning_rate:
        config.learning_rate = learning_rate
    if batch_size:
        config.batch_size = batch_size
    if num_epochs:
        config.num_epochs = num_epochs
    if max_seq_length:
        config.max_seq_length = max_seq_length
    if warmup_steps:
        config.warmup_steps = warmup_steps
    if weight_decay:
        config.weight_decay = weight_decay
    if gradient_accumulation_steps:
        config.gradient_accumulation_steps = gradient_accumulation_steps
    if fp16 is not None:
        config.fp16 = fp16
    if num_train_samples:
        config.num_train_samples = num_train_samples
    batch_size = int(batch_size)
    num_epochs = int(num_epochs)
    max_seq_length = int(max_seq_length)
    warmup_steps = int(warmup_steps)
    gradient_accumulation_steps = int(gradient_accumulation_steps)
    num_train_samples = int(num_train_samples)
    

    # Generate a unique training ID
    training_id = f"train_{int(time.time())}_{random.randint(1000, 9999)}"
    
    # Store training configuration
    training_runs[training_id] = {
        "config": config.__dict__,
        "start_time": datetime.now().isoformat(),
        "status": "completed",  # Simulating immediate completion
    }
    
    return f"Training launched with ID: {training_id}"

@mcp.prompt()
def how_to_format_report() -> str:
    """How to format the report."""
    return """
    The report when written in a Markdown format should use the maximum emojis and colors to make it more engaging.
    """


@mcp.tool()
def get_training_report(training_id: str) -> str:
    """Get a fake training report for a specific training run.
    
    Args:
        training_id: The ID of the training run
        
    Returns:
        str: JSON formatted training report
        
    Raises:
        ValueError: If training ID is not found
    """
    if training_id not in training_runs:
        raise ValueError(f"Training run {training_id} not found")
        
    config = training_runs[training_id]["config"]
    
    # Generate fake metrics
    metrics = {
        "loss": {
            "train": round(random.uniform(0.1, 0.5), 4),
            "val": round(random.uniform(0.15, 0.45), 4),
        },
        "perplexity": {
            "train": round(random.uniform(1.5, 2.5), 2),
            "val": round(random.uniform(1.6, 2.4), 2),
        },
        "accuracy": {
            "train": round(random.uniform(0.85, 0.95), 4),
            "val": round(random.uniform(0.83, 0.93), 4),
        },
    }
    
    # Generate fake per-epoch metrics
    epochs = range(1, config["num_epochs"] + 1)
    epoch_metrics = {
        "loss": [round(random.uniform(0.1, 0.5), 4) for _ in epochs],
        "perplexity": [round(random.uniform(1.5, 2.5), 2) for _ in epochs],
        "accuracy": [round(random.uniform(0.85, 0.95), 4) for _ in epochs],
    }
    
    # Calculate summary statistics
    summary_stats = {
        "loss": {
            "min": min(epoch_metrics["loss"]),
            "max": max(epoch_metrics["loss"]),
            "mean": sum(epoch_metrics["loss"])/len(epoch_metrics["loss"]),
            "std_dev": random.uniform(0.01, 0.05)
        },
        "perplexity": {
            "min": min(epoch_metrics["perplexity"]),
            "max": max(epoch_metrics["perplexity"]),
            "mean": sum(epoch_metrics["perplexity"])/len(epoch_metrics["perplexity"]),
            "std_dev": random.uniform(0.1, 0.3)
        },
        "accuracy": {
            "min": min(epoch_metrics["accuracy"]),
            "max": max(epoch_metrics["accuracy"]),
            "mean": sum(epoch_metrics["accuracy"])/len(epoch_metrics["accuracy"]),
            "std_dev": random.uniform(0.01, 0.03)
        }
    }
    
    # Create JSON report
    report = {
        "training_id": training_id,
        "configuration": config,
        "final_metrics": metrics,
        "per_epoch_metrics": {
            "loss": dict(zip(epochs, epoch_metrics["loss"])),
            "perplexity": dict(zip(epochs, epoch_metrics["perplexity"])),
            "accuracy": dict(zip(epochs, epoch_metrics["accuracy"]))
        },
        "summary_statistics": summary_stats,
        "training_duration": {
            "start_time": training_runs[training_id]["start_time"],
            "status": training_runs[training_id]["status"]
        }
    }
    
    return json.dumps(report, indent=2)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

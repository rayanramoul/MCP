# AI Server Training Run Report

## Training ID
`train_1750334590_9151`

## Configuration
```json
{
  "model_name": "gpt-3.5-turbo",
  "learning_rate": 0.0001,
  "batch_size": 32,
  "num_epochs": 10,
  "max_seq_length": 2048,
  "warmup_steps": 1000,
  "weight_decay": 0.01,
  "gradient_accumulation_steps": 4,
  "fp16": true,
  "num_train_samples": 1000000
}
```

## Final Metrics
| Metric      | Train   | Validation |
|-------------|---------|------------|
| Loss        | 0.4651  | 0.2488     |
| Perplexity  | 2.45    | 1.91       |
| Accuracy    | 0.8529  | 0.9106     |

## Per-Epoch Metrics
### Loss
| Epoch | Value  |
|-------|--------|
| 1     | 0.4529 |
| 2     | 0.3239 |
| 3     | 0.4671 |
| 4     | 0.4708 |
| 5     | 0.2225 |
| 6     | 0.3681 |
| 7     | 0.3902 |
| 8     | 0.1734 |
| 9     | 0.3980 |
| 10    | 0.4181 |

### Perplexity
| Epoch | Value |
|-------|-------|
| 1     | 1.59  |
| 2     | 1.98  |
| 3     | 2.09  |
| 4     | 2.04  |
| 5     | 2.18  |
| 6     | 2.19  |
| 7     | 2.47  |
| 8     | 1.67  |
| 9     | 2.34  |
| 10    | 1.71  |

### Accuracy
| Epoch | Value  |
|-------|--------|
| 1     | 0.9083 |
| 2     | 0.8783 |
| 3     | 0.8871 |
| 4     | 0.8904 |
| 5     | 0.9047 |
| 6     | 0.8971 |
| 7     | 0.9068 |
| 8     | 0.9036 |
| 9     | 0.9112 |
| 10    | 0.9251 |

## Summary Statistics
### Loss
- Min: 0.1734
- Max: 0.4708
- Mean: 0.3685
- Std Dev: 0.0485

### Perplexity
- Min: 1.59
- Max: 2.47
- Mean: 2.026
- Std Dev: 0.2837

### Accuracy
- Min: 0.8783
- Max: 0.9251
- Mean: 0.9013
- Std Dev: 0.0119

## Training Duration
- Start Time: 2025-06-19T14:03:10.629559
- Status: completed

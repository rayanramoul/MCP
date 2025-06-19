# AI Server Training Run Report

## Training ID
`train_1750346506_8095`

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
| Loss        | 0.1583  | 0.1617     |
| Perplexity  | 2.38    | 2.08       |
| Accuracy    | 0.9391  | 0.8806     |

## Per-Epoch Metrics
### Loss
| Epoch | Value  |
|-------|--------|
| 1     | 0.3765 |
| 2     | 0.2616 |
| 3     | 0.3148 |
| 4     | 0.3536 |
| 5     | 0.1501 |
| 6     | 0.1192 |
| 7     | 0.3791 |
| 8     | 0.4712 |
| 9     | 0.1830 |
| 10    | 0.3073 |

### Perplexity
| Epoch | Value |
|-------|-------|
| 1     | 1.94  |
| 2     | 2.46  |
| 3     | 2.19  |
| 4     | 2.05  |
| 5     | 1.83  |
| 6     | 2.33  |
| 7     | 1.67  |
| 8     | 2.13  |
| 9     | 2.33  |
| 10    | 1.73  |

### Accuracy
| Epoch | Value  |
|-------|--------|
| 1     | 0.8915 |
| 2     | 0.8569 |
| 3     | 0.8803 |
| 4     | 0.9460 |
| 5     | 0.8837 |
| 6     | 0.8727 |
| 7     | 0.8666 |
| 8     | 0.8550 |
| 9     | 0.8708 |
| 10    | 0.9377 |

## Summary Statistics
### Loss
- Min: 0.1192
- Max: 0.4712
- Mean: 0.2916
- Std Dev: 0.0156

### Perplexity
- Min: 1.67
- Max: 2.46
- Mean: 2.066
- Std Dev: 0.2751

### Accuracy
- Min: 0.8550
- Max: 0.9460
- Mean: 0.8861
- Std Dev: 0.0156

## Training Duration
- Start Time: 2025-06-19T17:21:46.927447
- Status: completed

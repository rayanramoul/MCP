# AI Server Training Run Report

## Training ID
`train_1750181610_4999`

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
| Loss        | 0.4799  | 0.2        |
| Perplexity  | 2.44    | 1.61       |
| Accuracy    | 0.9132  | 0.9236     |

## Per-Epoch Metrics
### Loss
| Epoch | Value  |
|-------|--------|
| 1     | 0.3072 |
| 2     | 0.3342 |
| 3     | 0.3086 |
| 4     | 0.4931 |
| 5     | 0.3918 |
| 6     | 0.3586 |
| 7     | 0.3863 |
| 8     | 0.19   |
| 9     | 0.2085 |
| 10    | 0.2783 |

### Perplexity
| Epoch | Value |
|-------|-------|
| 1     | 1.96  |
| 2     | 1.75  |
| 3     | 1.8   |
| 4     | 1.84  |
| 5     | 2.43  |
| 6     | 2.33  |
| 7     | 2.5   |
| 8     | 1.81  |
| 9     | 1.55  |
| 10    | 1.56  |

### Accuracy
| Epoch | Value   |
|-------|---------|
| 1     | 0.9046  |
| 2     | 0.897   |
| 3     | 0.8664  |
| 4     | 0.9091  |
| 5     | 0.939   |
| 6     | 0.8752  |
| 7     | 0.9047  |
| 8     | 0.9383  |
| 9     | 0.9111  |
| 10    | 0.9436  |

## Summary Statistics
### Loss
- Min: 0.19
- Max: 0.4931
- Mean: 0.32566
- Std Dev: 0.0243

### Perplexity
- Min: 1.55
- Max: 2.5
- Mean: 1.953
- Std Dev: 0.2314

### Accuracy
- Min: 0.8664
- Max: 0.9436
- Mean: 0.9089
- Std Dev: 0.0178

## Training Duration
- Start Time: 2025-06-17T19:33:30.498201
- Status: completed

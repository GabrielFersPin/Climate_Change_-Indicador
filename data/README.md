# 📊 Dataset Directory

## Required Dataset

This project uses the **Climate Change Indicators** dataset from Kaggle.

### Download Instructions

1. Visit [Kaggle - Climate Change Earth Surface Temperature](https://www.kaggle.com/datasets/tarunrm09/climate-change-indicators)
2. Download the CSV file(s)
3. Place it in this directory

### Expected Files
```
data/
├── climate_data.csv
└── (other CSVs from Kaggle)
```

### Why Not in Git?

The dataset exceeds GitHub's file size limits. We provide:
- ✅ Download instructions
- ✅ SQL initialization scripts
- ✅ Full reproducibility via Docker

## Temporary Test Data

For initial testing without downloading:
```python
# In your notebook
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'year': range(1900, 2024),
    'temperature': np.random.randn(124) + 15,
    'co2': np.random.randn(124) * 50 + 400
})

df.to_csv('data/climate_sample.csv', index=False)
```

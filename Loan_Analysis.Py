# Initial Libraries

import numpy as np
import pandas as pd

# Import dataset
df = pd.read_csv("LAA.csv")

# Initial data exploration
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.isnull().sum())
print(df.to_string())

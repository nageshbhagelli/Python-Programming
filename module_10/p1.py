import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("Student_Dataset.csv")

# i. Missing values in each column
print("Missing values per column:")
print(df.isnull().sum())

# ii. Drop duplicate records and reset index
df = df.drop_duplicates().reset_index(drop=True)

# iii. Find GPA values less than 0 or greater than 10
invalid_gpa = df[(df['GPA'] < 0) | (df['GPA'] > 10)]
print("\nInvalid GPA rows:")
print(invalid_gpa)

# iv. Replace such outliers with NaN, then fill NaN with mean
df.loc[(df['GPA'] < 0) | (df['GPA'] > 10), 'GPA'] = np.nan
mean_gpa = df['GPA'].mean()
df['GPA'] = df['GPA'].fillna(mean_gpa)
# To verify:
print("\nAfter replacing outliers, missing GPA filled with mean:")
print(df['GPA'].describe())
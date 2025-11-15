import numpy as np 
import pandas as pd
import os

# Setup paths (adjust as necessary)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, "Adult Dataset", "adult.data")
output_folder = os.path.join(project_root, "output")

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define column names for Adult dataset
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

# Load data into df
df = pd.read_csv(data_path, names=column_names, skipinitialspace=True, na_values=["?"])
print(f"Dataset loaded with shape: {df.shape}")

print("Detecting outliers...")
outlier_file = os.path.join(output_folder, "outliers_report.csv")

outlier_results = []
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    outlier_results.append({
        'Column': col,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'Lower_Bound': lower_bound,
        'Upper_Bound': upper_bound,
        'Outlier_Count': len(outliers),
        'Outlier_Percentage': (len(outliers)/len(df)*100)
    })

outlier_df = pd.DataFrame(outlier_results)
outlier_df.to_csv(outlier_file, index=False)

total_outliers = outlier_df['Outlier_Count'].sum()
print(f"      ✓ Found {total_outliers:,} total outliers across {len(numerical_cols)} numerical features")
print(f"      ✓ Report saved to: {os.path.basename(outlier_file)}\n")

# Optional: quick summary in console
print(outlier_df[['Column', 'Outlier_Count', 'Outlier_Percentage']])

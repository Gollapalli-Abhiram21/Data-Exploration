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

# Load data into df (this must happen before any use of df)
df = pd.read_csv(data_path, names=column_names, skipinitialspace=True)

print(f"Dataset loaded with shape: {df.shape}")

# Now perform missing value analysis
missing_counts = {}
for col in df.columns:
    if df[col].dtype == 'object':
        missing_count = (df[col] == '?').sum()
    else:
        missing_count = df[col].isnull().sum()
    missing_counts[col] = missing_count

missing_df = pd.DataFrame({
    'Column': missing_counts.keys(),
    'Missing_Count': missing_counts.values(),
    'Percentage': [(v / len(df) * 100) for v in missing_counts.values()]
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

# Save missing values report
missing_file = os.path.join(output_folder, "missing_values_report.csv")
missing_df.to_csv(missing_file, index=False)

print(f"✓ Found {sum(missing_counts.values()):,} missing values in {len(missing_df)} columns")
print(f"✓ Report saved to: {missing_file}")



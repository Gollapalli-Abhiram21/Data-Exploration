import pandas as pd
import os
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

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

# Group by income and calculate statistics
hours_analysis = df.groupby('income')['hours-per-week'].agg([
    'mean', 'median', 'std', 'min', 'max'
]).round(2)

print("Hours per Week by Income Level:")
print(hours_analysis)

# Statistical test - Are the differences significant?

low_income_hours = df[df['income'] == '<=50K']['hours-per-week']
high_income_hours = df[df['income'] == '>50K']['hours-per-week']

t_stat, p_value = stats.ttest_ind(low_income_hours, high_income_hours)
print(f"\nT-test results:")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("✓ Significant difference in working hours between income groups")
else:
    print("✗ No significant difference")

# Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='income', y='hours-per-week', data=df)
plt.title('Working Hours by Income Level')
plt.ylabel('Hours per Week')
plt.xlabel('Income Category')

# Save the file BEFORE showing
output_file = os.path.join(output_folder, "hours_income_analysis.png")
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Graph saved to: {output_file}")

# Now show the plot
plt.show()


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

# Encode income as binary
df['income_binary'] = df['income'].apply(lambda x: 1 if x == '>50K' else 0)

# Calculate correlation with income
numerical_features = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                     'capital-loss', 'hours-per-week']

correlations = {}
for feature in numerical_features:
    corr = df[feature].corr(df['income_binary'])
    correlations[feature] = corr

# Sort by absolute correlation
corr_sorted = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)

print("Features Correlated with Income (sorted by strength):")
print("-" * 60)
for feature, corr in corr_sorted:
    strength = "Strong" if abs(corr) > 0.3 else "Moderate" if abs(corr) > 0.1 else "Weak"
    direction = "Positive" if corr > 0 else "Negative"
    print(f"{feature:20s}: {corr:6.3f} ({strength} {direction})")

# Visualization
plt.figure(figsize=(10, 6))
features = [item[0] for item in corr_sorted]
values = [item[1] for item in corr_sorted]

plt.barh(features, values, color=['green' if v > 0 else 'red' for v in values])
plt.xlabel('Correlation with Income')
plt.title('Feature Correlation with Earning Potential')
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)

# Save the file BEFORE showing
output_file = os.path.join(output_folder, "feature_income_analysis.png")
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Graph saved to: {output_file}")

# Now show the plot
plt.show()

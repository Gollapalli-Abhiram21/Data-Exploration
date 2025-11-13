"""
Adult Dataset - Data Exploration with File Outputs
===================================================
This script performs data exploration and saves all results to the output folder.
Only progress messages are displayed in the console.


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
from datetime import datetime
warnings.filterwarnings('ignore')

# Configure display and plotting
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Print header
print("\n" + "="*80)
print("ADULT DATASET - DATA EXPLORATION AND ANALYSIS")
print("="*80)
print("Starting process...\n")

# ==================== SETUP ====================
# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, "Adult Dataset", "adult.data")
output_dir = os.path.join(project_root, "output")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Column names
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

# ==================== LOAD DATA ====================
print("[1/6] Loading dataset...")
df = pd.read_csv(data_path, names=column_names, skipinitialspace=True)
print(f"      ✓ Loaded {len(df):,} records with {len(df.columns)} features\n")

# ==================== EXPLORATION SUMMARY ====================
print("[2/6] Generating exploration summary...")
summary_file = os.path.join(output_dir, "exploration_summary.txt")

with open(summary_file, 'w') as f:
    f.write("="*80 + "\n")
    f.write("ADULT DATASET - EXPLORATION SUMMARY\n")
    f.write("="*80 + "\n\n")
    
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("DATASET OVERVIEW\n")
    f.write("-"*80 + "\n")
    f.write(f"Total Records: {len(df):,}\n")
    f.write(f"Total Features: {len(df.columns)}\n")
    f.write(f"Dataset Shape: {df.shape}\n\n")
    
    f.write("COLUMN NAMES\n")
    f.write("-"*80 + "\n")
    for i, col in enumerate(df.columns, 1):
        f.write(f"{i:2d}. {col}\n")
    
    f.write("\n\nFIRST 10 ROWS\n")
    f.write("-"*80 + "\n")
    f.write(df.head(10).to_string())
    
    f.write("\n\n\nDATA TYPES\n")
    f.write("-"*80 + "\n")
    f.write(df.dtypes.to_string())

print(f"      ✓ Summary saved to: {os.path.basename(summary_file)}\n")

# ==================== STATISTICAL SUMMARY ====================
print("[3/6] Generating statistical summary...")
stats_file = os.path.join(output_dir, "statistical_summary.csv")

# Numerical statistics
numerical_stats = df.describe().T
numerical_stats.to_csv(stats_file)

print(f"      ✓ Statistics saved to: {os.path.basename(stats_file)}\n")

# ==================== MISSING VALUES ANALYSIS ====================
print("[4/6] Analyzing missing values...")
missing_file = os.path.join(output_dir, "missing_values_report.csv")

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
    'Percentage': [(v/len(df)*100) for v in missing_counts.values()]
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
missing_df.to_csv(missing_file, index=False)

total_missing = sum(missing_counts.values())
rows_with_missing = df[df.isin(['?']).any(axis=1)].shape[0]

print(f"      ✓ Found {total_missing:,} missing values in {len(missing_df)} columns")
print(f"      ✓ {rows_with_missing:,} rows contain at least one missing value")
print(f"      ✓ Report saved to: {os.path.basename(missing_file)}\n")

# ==================== OUTLIER DETECTION ====================
print("[5/6] Detecting outliers...")
outlier_file = os.path.join(output_dir, "outliers_report.csv")

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

# ==================== VISUALIZATIONS ====================
print("[6/6] Generating visualizations...")

# 1. Age Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=30, edgecolor='black', color='skyblue')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Age Distribution', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
age_plot = os.path.join(output_dir, "age_distribution.png")
plt.savefig(age_plot, dpi=300, bbox_inches='tight')
plt.close()

# 2. Income Distribution
plt.figure(figsize=(8, 6))
income_counts = df['income'].value_counts()
plt.bar(income_counts.index, income_counts.values, color=['coral', 'lightgreen'])
plt.xlabel('Income Category', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Income Distribution', fontsize=14, fontweight='bold')
for i, v in enumerate(income_counts.values):
    plt.text(i, v + 1000, f'{v:,}', ha='center', fontsize=11)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
income_plot = os.path.join(output_dir, "income_distribution.png")
plt.savefig(income_plot, dpi=300, bbox_inches='tight')
plt.close()

# 3. Hours per Week by Income (Box Plot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='income', y='hours-per-week', data=df, palette='Set2')
plt.xlabel('Income Category', fontsize=12)
plt.ylabel('Hours per Week', fontsize=12)
plt.title('Working Hours by Income Level', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
hours_plot = os.path.join(output_dir, "hours_by_income.png")
plt.savefig(hours_plot, dpi=300, bbox_inches='tight')
plt.close()

# 4. Education Distribution
plt.figure(figsize=(14, 6))
education_counts = df['education'].value_counts()
plt.bar(range(len(education_counts)), education_counts.values, color='steelblue')
plt.xlabel('Education Level', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Education Level Distribution', fontsize=14, fontweight='bold')
plt.xticks(range(len(education_counts)), education_counts.index, rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
edu_plot = os.path.join(output_dir, "education_distribution.png")
plt.savefig(edu_plot, dpi=300, bbox_inches='tight')
plt.close()

# 5. Correlation Heatmap
numerical_features = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                     'capital-loss', 'hours-per-week']
correlation_matrix = df[numerical_features].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
corr_plot = os.path.join(output_dir, "correlation_heatmap.png")
plt.savefig(corr_plot, dpi=300, bbox_inches='tight')
plt.close()

print(f"      ✓ Generated 5 visualization files\n")

# ==================== COMPLETION ====================
print("="*80)
print("PROCESS COMPLETED SUCCESSFULLY")
print("="*80)
print(f"\nAll outputs saved to: {output_dir}")
print("\nGenerated Files:")
print("  1. exploration_summary.txt      - Dataset overview and first rows")
print("  2. statistical_summary.csv      - Descriptive statistics")
print("  3. missing_values_report.csv    - Missing values analysis")
print("  4. outliers_report.csv          - Outlier detection results")
print("  5. age_distribution.png         - Age histogram")
print("  6. income_distribution.png      - Income bar chart")
print("  7. hours_by_income.png          - Working hours box plot")
print("  8. education_distribution.png   - Education bar chart")
print("  9. correlation_heatmap.png      - Feature correlations")
print("\n" + "="*80 + "\n")

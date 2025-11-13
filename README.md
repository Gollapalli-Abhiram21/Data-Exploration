# Adult Dataset - Data Exploration and Analysis

This project performs comprehensive data exploration and analysis on the **Adult Census Income Dataset** to help a company study demographic data and make predictions about the earning potential of the population. The dataset contains demographic and employment information that needs to be cleaned and analyzed for data-driven competitive advantage.

## 🎯 Project Objectives

The company has requested the following operations to be performed:

1. **Remove data with missing values** - Clean the dataset by handling missing entries
2. **Remove outliers** - Identify and remove statistical outliers that could skew analysis
3. **Establish the importance of weekly working hours on earning potential** - Analyze correlation
4. **Find features highly correlated with earning potential** - Feature importance analysis
5. **Find the relation between years spent getting a degree and earning potential** - Education analysis
6. **Find the relationship between age and earning potential** - Age demographics analysis

## 📁 Project Structure

```
data_exploration/
│
├── Adult Dataset/
│   ├── adult.data          # Main dataset file
│   └── adult.names         # Dataset documentation and column descriptions
│
├── scripts/
│   ├── clean_exploration.py   # Main exploration script (recommended)
│   ├── age_vs_income.py # Age demographics analysis 
│   ├── missing_values.py # Missing values report
│   ├── outlier_detection.py # IQR-based outlier removal
│   ├── education_vs_income.py # Education level vs income analysis
│   ├── feature_importance_income.py # Feature correlation analysis 
│   └── hours_vs_income_correlation.py # Weekly working hours impact 

│
├── output/                  # Generated analysis results
│   ├── exploration_summary.txt
│   ├── statistical_summary.csv
│   ├── missing_values_report.csv
│   ├── outliers_report.csv
│   ├── age_distribution.png
│   ├── income_distribution.png
│   ├── hours_by_income.png
│   ├── education_distribution.png
│   ├── correlation_heatmap.png
│   ├── age_income_analysis.png
│   ├── feature_income_analysis.png
│   ├── education_income_analysis.png
│   └── hours_income_analysis.png
│
│
└── README.md               # This file - Project documentation
```

## 🔧 Technologies and Libraries Used

### Programming Language
- **Python 3.x** - Main programming language

### Data Analysis Libraries
- **pandas** - Data manipulation and analysis
  - Loading CSV files
  - Data cleaning and transformation
  - Statistical operations
  
- **numpy** - Numerical computing
  - Mathematical operations
  - Array manipulations

### Data Visualization Libraries
- **matplotlib** - Basic plotting and visualization
  - Creating charts and graphs
  - Customizing plot appearance
  
- **seaborn** - Statistical data visualization
  - Advanced statistical plots
  - Beautiful default styles

### Statistical Analysis
- **scipy.stats** - Statistical functions
  - Outlier detection
  - Statistical tests
  - Correlation analysis

### System Operations
- **os** - Operating system interface
  - Dynamic file path handling
  - Cross-platform compatibility

## 📋 Dataset Information

### Dataset Source
The Adult Census Income dataset (also known as "Census Income" dataset) from the UCI Machine Learning Repository.

### Features (Columns)
The dataset contains **15 columns**:

**Numerical Features:**
1. `age` - Age of the individual
2. `fnlwgt` - Final weight (number of people the census believes the entry represents)
3. `education-num` - Number of years of education
4. `capital-gain` - Capital gains
5. `capital-loss` - Capital losses
6. `hours-per-week` - Hours worked per week

**Categorical Features:**
7. `workclass` - Type of employment (Private, Self-emp, Government, etc.)
8. `education` - Highest level of education achieved
9. `marital-status` - Marital status
10. `occupation` - Type of occupation
11. `relationship` - Relationship status
12. `race` - Race
13. `sex` - Gender
14. `native-country` - Country of origin

**Target Variable:**
15. `income` - Income level (<=50K or >50K)

## 🚀 How to Run the Data Exploration Analysis

### Prerequisites

1. **Install Python** (version 3.7 or higher)
   - Download from [python.org](https://www.python.org/downloads/)

2. **Install Required Libraries**
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

### Running the Analysis

#### Method 1: Using PowerShell (Windows) - Recommended

1. Open PowerShell
2. Navigate to the project directory (replace with your actual path):
   ```powershell
   cd "path\to\your\data_exploration"
   ```
   Example:
   ```powershell
   cd "C:\Projects\data_exploration"
   ```

3. Run the clean exploration script (recommended):
   ```powershell
   python .\scripts\02_clean_exploration.py
   ```
   
   This will:
   - Show clean progress messages in console
   - Generate all output files in the `output` folder
   - Create 4 CSV/text reports and 5 visualization images

   **Alternative:** Run with detailed console output:
   ```powershell
   python .\scripts\data_exploration.py
   ```

#### Method 2: From the Scripts Directory

1. Navigate to the scripts folder (replace with your actual path):
   ```powershell
   cd "path\to\your\data_exploration\scripts"
   ```

2. Run the script:
   ```powershell
   python .\02_clean_exploration.py
   ```
   Or for detailed output:
   ```powershell
   python .\01_data_exploration.py
   ```

#### Method 3: Using VS Code

1. Open the project folder in VS Code
2. Open the file `scripts/clean_exploration.py`
3. Press `F5` or click "Run" → "Run Without Debugging"
4. Check the `output` folder for generated files

## 📂 Understanding the Output Files

After running the script, the `output` folder will contain:

### Text and CSV Reports

1. **exploration_summary.txt**
   - Dataset overview (rows, columns, shape)
   - First 10 rows of data
   - Column names and data types
   - Useful for: Quick understanding of the dataset

2. **statistical_summary.csv**
   - Descriptive statistics for all numerical features
   - Includes: count, mean, std, min, 25%, 50%, 75%, max
   - Useful for: Understanding data distribution and ranges

3. **missing_values_report.csv**
   - Lists columns with missing values
   - Shows count and percentage of missing data
   - Useful for: Data cleaning decisions

4. **outliers_report.csv**
   - Outlier detection results using IQR method
   - Shows Q1, Q3, IQR, bounds, and outlier counts
   - Useful for: Identifying anomalous data points

### Visualization Files (PNG Images)

5. **age_distribution.png**
   - Histogram showing age distribution
   - Useful for: Understanding age demographics

6. **income_distribution.png**
   - Bar chart of income categories (<=50K vs >50K)
   - Useful for: Understanding target variable balance

7. **hours_by_income.png**
   - Box plot comparing working hours by income level
   - Useful for: Seeing relationship between hours worked and income

8. **education_distribution.png**
   - Bar chart of education level distribution
   - Useful for: Understanding education patterns in dataset

9. **correlation_heatmap.png**
   - Correlation matrix of numerical features
   - Useful for: Finding relationships between variables

10. **education_income_analysis.png**
   - Education level vs income level
   - Often a strong predictor

11. **age_income_analysis.png**
   - Can reveal non-linear trene
   - e.g, mid-career peak earnings

12. **feature_income_analysis.png**
   - Correlation matrix of numerical features
   - Useful for: Feature selection


## 📝 What the Script Does

### Clean Exploration Script (clean_exploration.py) - Recommended

This script provides a clean, professional output experience:

**Console Output:**
- ✅ Shows progress: [1/6], [2/6], etc.
- ✅ Displays only essential information
- ✅ Confirms when each file is generated
- ✅ Lists all output files at the end
- ❌ No lengthy data dumps in terminal

**File Outputs:**
- ✅ Saves all analysis results to files
- ✅ Creates visualization images
- ✅ Generates CSV reports for further analysis
- ✅ All outputs organized in `output` folder

### Step-by-Step Process

#### **Step 1: Data Loading** [1/6]
- Uses dynamic file paths (works on any system)
- Loads the CSV file with proper column names
- Displays record count and feature count
- **Output:** Confirmation message only

#### **Step 2: Exploration Summary** [2/6]
- Generates comprehensive text summary
- Includes dataset shape, column names, data types
- Shows first 10 rows for quick inspection
- **Output:** `exploration_summary.txt`

#### **Step 3: Statistical Summary** [3/6]
- Calculates descriptive statistics for all numerical features
- Includes mean, median, std, min, max, quartiles
- **Output:** `statistical_summary.csv`

#### **Step 4: Missing Values Analysis** [4/6]
- Detects missing values (represented as '?' in this dataset)
- Calculates count and percentage per column
- Shows total affected rows
- **Output:** `missing_values_report.csv`
- **Console:** Shows count of missing values found

#### **Step 5: Outlier Detection** [5/6]
- Uses the **IQR (Interquartile Range) Method**
- Calculates Q1, Q3, IQR for each numerical feature
- Identifies outliers beyond 1.5×IQR from quartiles
- **Output:** `outliers_report.csv`
- **Console:** Shows total outlier count

#### **Step 6: Visualizations** [6/6]
- Creates 5 high-quality PNG images:
  - Age distribution histogram
  - Income distribution bar chart
  - Working hours by income box plot
  - Education distribution bar chart
  - Correlation heatmap
- **Output:** 5 PNG files (300 DPI, publication quality)
- **Console:** Confirms all visualizations generated

## 🔍 Key Findings from Initial Exploration

After running the script, you will discover:

1. **Missing Values**: Some columns contain '?' representing missing data
   - Need to be removed or imputed

2. **Outliers Present**: Several numerical features have outliers
   - Examples: extreme values in capital-gain, hours-per-week
   - May need to be handled based on business context

3. **Class Imbalance**: Income distribution may be imbalanced
   - More people earning <=50K than >50K
   - Important for prediction modeling

4. **Data Quality Issues**: 
   - Whitespace in categorical values
   - Inconsistent formatting
   - Will be addressed in cleaning phase

## 🔄 Next Steps

After completing the initial exploration:

1. **Data Cleaning**:
   - Remove or impute missing values
   - Handle outliers appropriately
   - Standardize categorical values

2. **Feature Engineering**:
   - Create new meaningful features
   - Encode categorical variables
   - Scale numerical features

3. **Statistical Analysis**:
   - Correlation analysis between features and income
   - Hypothesis testing
   - Feature importance ranking

4. **Visualization**:
   - Create plots to visualize relationships
   - Distribution plots
   - Correlation heatmaps

5. **Modeling** (Future):
   - Build predictive models
   - Evaluate model performance
   - Make predictions on new data

## 💡 Understanding the Code

### Dynamic File Paths
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, "Adult Dataset", "adult.data")
```

**Why use dynamic paths?**
- **Portability**: Code runs on any computer without modification
- **Cross-platform**: Works on Windows, Mac, and Linux
- **Flexibility**: Project can be moved to any location

**How it works:**
1. `__file__` - Path to the current script
2. `os.path.abspath(__file__)` - Gets absolute path
3. `os.path.dirname()` - Gets the directory containing the file
4. `os.path.join()` - Combines paths using OS-appropriate separators

### IQR Method for Outlier Detection
```python
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```

**Why IQR method?**
- **Robust**: Not affected by extreme outliers
- **Standard**: Widely used statistical method
- **Visual**: Forms the basis of box plots
- **Interpretable**: Clear mathematical definition

## 🛠️ Troubleshooting

### Common Issues and Solutions

**Issue 1: ModuleNotFoundError**
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution**: Install missing libraries
```bash
pip install pandas numpy matplotlib seaborn scipy
```

**Issue 2: File Not Found Error**
```
FileNotFoundError: [Errno 2] No such file or directory
```
**Solution**: 
- Ensure the dataset file exists in `Adult Dataset/adult.data`
- Check folder structure matches the expected layout

**Issue 3: Display Issues in Terminal**
```
Truncated output or formatting issues
```
**Solution**: Run in a terminal with wider width or use VS Code integrated terminal

## 📚 Learning Resources

### Pandas Documentation
- [Official Pandas Docs](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### Data Analysis Tutorials
- [Real Python - Data Analysis](https://realpython.com/learning-paths/data-analysis-python/)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Statistical Concepts
- [Understanding Outliers](https://www.statisticshowto.com/statistics-basics/find-outliers/)
- [Exploratory Data Analysis](https://www.ibm.com/cloud/learn/exploratory-data-analysis)

## 👤 Author

Abhiram Gollapalli

## 📄 License

This project is for educational and business analysis purposes.

---

**Last Updated**: November 2025

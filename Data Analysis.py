# Exploratory Data Analysis (EDA) - Descriptive Statistics, Visualization, Missing Data, and Outliers
# Experiment 12: Based on the comprehensive EDA guidelines covering descriptive statistics, visualization, missing data handling, and outlier management

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def perform_eda():
    # Sample dataset with missing values and outliers for demonstration
    data = {
        'Age': [24, 27, 22, 32, 29, 25, 100, None, 31],
        'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 600000, 53000, None]
    }
    df = pd.DataFrame(data)
    print("--- Original DataFrame ---")
    print(df)
    print("\n")

    # 1. Descriptive Statistics
    print("--- Descriptive Statistics ---")
    print(df.describe())
    print("Mean Age:", df['Age'].mean())
    print("Median Age:", df['Age'].median())
    print("Standard Deviation of Age:", df['Age'].std())
    print("\n")

    # 2. Handling Missing Data
    print("--- Handling Missing Data (Filling with Mean) ---")
    df_filled = df.fillna(df.mean(numeric_only=True))
    print(df_filled)
    print("\n")

    # 3. Handling Outliers using Z-scores
    print("--- Handling Outliers (Z-score method) ---")
    df_filled['Age_zscore'] = zscore(df_filled['Age'])
    df_filled['Salary_zscore'] = zscore(df_filled['Salary'])
    
    # Filter rows where absolute z-score <= 3
    df_no_outliers = df_filled[(df_filled['Age_zscore'].abs() <= 3) & (df_filled['Salary_zscore'].abs() <= 3)]
    print(df_no_outliers[['Age', 'Salary']])
    print("\n")

    # 4. Visualization & Plotting (Code structure as outlined in theory)
    print("Generating visualizations...")
    plt.figure(figsize=(12, 4))

    # Histogram of Age
    plt.subplot(1, 3, 1)
    plt.hist(df_filled['Age'].dropna(), bins=5, edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # Box Plot of Age
    plt.subplot(1, 3, 2)
    sns.boxplot(y=df_filled['Age'])
    plt.title('Box Plot of Age')

    # Scatter Plot of Age vs Salary
    plt.subplot(1, 3, 3)
    plt.scatter(df_filled['Age'], df_filled['Salary'])
    plt.title('Age vs Salary')
    plt.xlabel('Age')
    plt.ylabel('Salary')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    perform_eda()
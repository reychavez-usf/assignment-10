# Module 10 Assignment: Data Manipulation and Cleaning with Pandas
# UrbanStyle Customer Data Cleaning

# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

# Welcome message
print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
from io import StringIO

# Simulated CSV content with intentional data issues
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver
"""

# Create a StringIO object (simulates a file)
customer_data_csv = StringIO(csv_content)

# Now you can load this as if it was a CSV file:
# raw_df = pd.read_csv(customer_data_csv)
# ----- END OF SIMULATION CODE -----


# TODO 1: Load and Explore the Dataset
# 1.1 Load the dataset and display basic information
# REQUIRED: Store DataFrame in variable 'raw_df'
# Your code here
raw_df = pd.read_csv(customer_data_csv)

print("Dataset Shape:", raw_df.shape)
print("\nColumn Names:", raw_df.columns.tolist())
print("\nData Types:\n", raw_df.dtypes)
print("\nFirst 5 Rows:\n", raw_df.head())
print("\nDataset Info:")
raw_df.info()
print("\nBasic Statistics:\n", raw_df.describe(include='all'))

# 1.2 Assess the data quality issues (missing values, incorrect formats, duplicates)
# REQUIRED: Store initial missing value counts in 'initial_missing_counts' (pandas Series)
# REQUIRED: Store duplicate count in variable 'initial_duplicate_count' (int)
# Your code here
initial_missing_counts = raw_df.isnull().sum()
print("\nMissing Values Per Column:\n", initial_missing_counts)

initial_duplicate_count = raw_df.duplicated().sum()
print("\nNumber of Duplicate Rows:", initial_duplicate_count)

# TODO 2: Handle Missing Values
# 2.1 Identify and count missing values
# REQUIRED: Store in variable 'missing_value_report' (pandas Series)
# Your code here
missing_value_report = raw_df.isnull().sum()
print("Missing Value Report:")
print(missing_value_report[missing_value_report > 0])


# 2.2 Fill missing satisfaction_rating with the median value
# REQUIRED: Store median value used in variable 'satisfaction_median' (float)
# Your code here
satisfaction_median = raw_df['satisfaction_rating'].median()
print(f"\nSatisfaction Rating Median: {satisfaction_median}")
raw_df['satisfaction_rating'] = raw_df['satisfaction_rating'].fillna(satisfaction_median)


# 2.3 Fill missing last_purchase dates appropriately
# REQUIRED: Store strategy used in variable 'date_fill_strategy' (string: 'forward_fill', 'backward_fill', or 'drop')
# Your code here
date_fill_strategy = 'forward_fill'
raw_df['last_purchase'] = raw_df['last_purchase'].ffill()

# 2.4 Handle other missing values as needed
# REQUIRED: Store cleaned DataFrame in variable 'df_no_missing'
# Your code here
raw_df['last_name'] = raw_df['last_name'].fillna('Unknown')
raw_df['phone'] = raw_df['phone'].fillna('N/A')
raw_df['age'] = raw_df['age'].fillna(raw_df['age'].median())
raw_df['loyalty_status'] = raw_df['loyalty_status'].fillna('Bronze')

df_no_missing = raw_df.copy()
print("\nMissing values after cleaning:")
print(df_no_missing.isnull().sum())

# TODO 3: Correct Data Types
# 3.1 Convert join_date and last_purchase to datetime
# REQUIRED: Work with 'df_no_missing' and store result in 'df_typed'
# Your code here
df_typed = df_no_missing.copy()

df_typed['join_date'] = pd.to_datetime(df_typed['join_date'], format='mixed')
df_typed['last_purchase'] = pd.to_datetime(df_typed['last_purchase'], format='mixed')

print("Updated Data Types:")
print(df_typed[['join_date', 'last_purchase']].dtypes)
print("\nSample dates after conversion:")
print(df_typed[['join_date', 'last_purchase']].head())

# 3.2 Convert total_spent to numeric (handle currency symbols and commas)
# REQUIRED: Continue working with 'df_typed'
# Your code here
df_typed['total_spent'] = (
    df_typed['total_spent']
    .astype(str)             
    .str.replace('$', '', regex=False)   
    .str.replace(',', '', regex=False)   
    .astype(float)           
)

print("total_spent dtype:", df_typed['total_spent'].dtype)
print("\nConverted Sample Values:")
print(df_typed['total_spent'].head(10))

# 3.3 Ensure other numeric fields (total_purchases, age) are correct types
# REQUIRED: Store final typed DataFrame in 'df_typed'
# Your code here
df_typed['total_purchases'] = df_typed['total_purchases'].astype(int)
df_typed['age'] = df_typed['age'].astype(int)

print("Updated Data Types:")
print(df_typed[['total_purchases', 'age', 'total_spent']].dtypes)
print("\nSample values after conversion:")
print(df_typed[['total_purchases', 'age', 'total_spent']].head())

# TODO 4: Clean and Standardize Text Data
# 4.1 Standardize case for first_name and last_name (proper case)
# REQUIRED: Work with 'df_typed' and store result in 'df_text_cleaned'
# Your code here
df_text_cleaned = df_typed.copy()

df_text_cleaned['first_name'] = df_text_cleaned['first_name'].str.title()
df_text_cleaned['last_name'] = df_text_cleaned['last_name'].str.title()

print("Standardized Names:")
print(df_text_cleaned[['first_name', 'last_name']].to_string())

# 4.2 Standardize category names (consistent capitalization)
# REQUIRED: Continue working with 'df_text_cleaned'
# Your code here
df_text_cleaned['preferred_category'] = df_text_cleaned['preferred_category'].str.title()

print("Unique categories after standardization:")
print(df_text_cleaned['preferred_category'].unique())
print("\nCategory value counts:")
print(df_text_cleaned['preferred_category'].value_counts())

# 4.3 Standardize phone numbers to a consistent format
# REQUIRED: Store standardized phone format used in variable 'phone_format' (string)
# Your code here
df_text_cleaned['phone'] = df_text_cleaned['phone'].str.replace(r'\D', '', regex=True)
df_text_cleaned['phone'] = df_text_cleaned['phone'].replace('', 'N/A')
def phone_format(phone):
    if phone == 'N/A':
        return phone
    return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

phone_format = 'XXX-XXX-XXXX'

print(f"Phone format used: {phone_format}")
print("\nPhone numbers after standardization:")
print(df_text_cleaned[['first_name', 'last_name', 'phone']].to_string())
# TODO 5: Remove Duplicates
# 5.1 Identify duplicate records
# REQUIRED: Store duplicate count in variable 'duplicate_count' (int)
# Your code here
duplicate_count = df_text_cleaned.duplicated().sum()

print(f"Number of duplicate rows: {duplicate_count}")
print("\nDuplicate records:")
print(df_text_cleaned[df_text_cleaned.duplicated(keep=False)])

# 5.2 Remove duplicates while keeping the appropriate record
# REQUIRED: Work with 'df_text_cleaned' and store result in 'df_no_duplicates'
# Your code here
df_no_duplicates = df_text_cleaned.drop_duplicates(keep='first')

print(f"Rows before removing duplicates: {len(df_text_cleaned)}")
print(f"Rows after removing duplicates: {len(df_no_duplicates)}")
print(f"\nRows removed: {len(df_text_cleaned) - len(df_no_duplicates)}")
print("\nRemaining customers:")
print(df_no_duplicates[['customer_id', 'first_name', 'last_name']].to_string())

# TODO 6: Add Derived Features
# 6.1 Calculate days_since_last_purchase
# REQUIRED: Work with 'df_no_duplicates' and add column 'days_since_last_purchase'
# Your code here
reference_date = pd.Timestamp('2023-12-31')

df_no_duplicates['days_since_last_purchase'] = (
    reference_date - df_no_duplicates['last_purchase']
).dt.days

print("Days since last purchase:")
print(df_no_duplicates[['first_name', 'last_name', 'last_purchase', 'days_since_last_purchase']].to_string())

# 6.2 Calculate average_purchase_value (total_spent / total_purchases)
# REQUIRED: Add column 'average_purchase_value' to DataFrame
# Your code here
df_no_duplicates['average_purchase_value'] = np.where(
    df_no_duplicates['total_purchases'] > 0,
    df_no_duplicates['total_spent'] / df_no_duplicates['total_purchases'],
    0
)

df_no_duplicates['average_purchase_value'] = df_no_duplicates['average_purchase_value'].round(2)

print("Average purchase value per customer:")
print(df_no_duplicates[['first_name', 'last_name', 'total_spent', 'total_purchases', 'average_purchase_value']].to_string())

# 6.3 Create a purchase_frequency_category (High, Medium, Low)
# REQUIRED: Add column 'purchase_frequency_category' using these rules:
# - High: >= 10 purchases
# - Medium: 5-9 purchases
# - Low: < 5 purchases
# Your code here
df_no_duplicates['purchase_frequency_category'] = pd.cut(
    df_no_duplicates['total_purchases'],
    bins=[-1, 4, 9, float('inf')],
    labels=['Low', 'Medium', 'High']
)

print("Purchase frequency categories:")
print(df_no_duplicates[['first_name', 'last_name', 'total_purchases', 'purchase_frequency_category']].to_string())

print("\nCategory counts:")
print(df_no_duplicates['purchase_frequency_category'].value_counts())

# TODO 7: Clean Up the DataFrame
# 7.1 Rename columns to more readable formats
# REQUIRED: Store renamed DataFrame in 'df_renamed'
# Your code here
df_renamed = df_no_duplicates.rename(columns={
    'customer_id'                : 'Customer ID',
    'first_name'                 : 'First Name',
    'last_name'                  : 'Last Name',
    'email'                      : 'Email',
    'phone'                      : 'Phone',
    'join_date'                  : 'Join Date',
    'last_purchase'              : 'Last Purchase Date',
    'total_purchases'            : 'Total Purchases',
    'total_spent'                : 'Total Spent',
    'preferred_category'         : 'Preferred Category',
    'satisfaction_rating'        : 'Satisfaction Rating',
    'age'                        : 'Age',
    'city'                       : 'City',
    'state'                      : 'State',
    'loyalty_status'             : 'Loyalty Status',
    'days_since_last_purchase'   : 'Days Since Last Purchase',
    'average_purchase_value'     : 'Average Purchase Value',
    'purchase_frequency_category': 'Purchase Frequency'
})

print("Renamed columns:")
print(df_renamed.columns.tolist())

# 7.2 Remove any unnecessary columns
# REQUIRED: Store cleaned DataFrame in 'df_final'
# Your code here
print("Current columns:")
for col in df_renamed.columns.tolist():
    print(f"  - {col}")

df_final = df_renamed.copy()

print(f"\nFinal DataFrame shape: {df_final.shape}")
print(f"Total columns: {len(df_final.columns)}")
print(f"Total customers: {len(df_final)}")
# 7.3 Sort the data by a meaningful attribute
# REQUIRED: Sort 'df_final' by total_spent descending and store in 'df_final'
# Your code here
df_final = df_final.sort_values(by='Total Spent', ascending=False)

print("DataFrame sorted by Total Spent (highest to lowest):")
print(df_final[['First Name', 'Last Name', 'Total Spent', 'Loyalty Status']].to_string())

# TODO 8: Generate Insights from Cleaned Data
# 8.1 Calculate average spent by loyalty_status
# REQUIRED: Store result in 'avg_spent_by_loyalty' (pandas Series)
# Your code here
avg_spent_by_loyalty = df_final.groupby('Loyalty Status')['Total Spent'].mean().round(2)

print("Average Total Spent by Loyalty Status:")
print(avg_spent_by_loyalty.sort_values(ascending=False))

# 8.2 Find top preferred categories by total_spent
# REQUIRED: Store result in 'category_revenue' (pandas Series, sorted descending)
# Your code here
category_revenue = df_final.groupby('Preferred Category')['Total Spent'].sum().round(2).sort_values(ascending=False)

print("Total Revenue by Preferred Category:")
print(category_revenue)

# 8.3 Calculate correlation between satisfaction_rating and total_spent
# REQUIRED: Store correlation value in 'satisfaction_spend_corr' (float)
# Your code here
satisfaction_spend_corr = df_final['Satisfaction Rating'].corr(df_final['Total Spent']).round(4)

print(f"Correlation between Satisfaction Rating and Total Spent: {satisfaction_spend_corr}")

# TODO 9: Generate Final Report
print("\n" + "=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING REPORT")
print("=" * 60)

# 9.1 Report on data quality issues found and how they were addressed
# REQUIRED OUTPUT FORMAT:
# Data Quality Issues:
# - Missing Values: X total missing entries
# - Duplicates: X duplicate records found
# - Data Type Issues: [list issues]
# Your code here
print("\nData Quality Issues:")
print(f"  - Missing Values: {initial_missing_counts.sum()} total missing entries")
print(f"  - Duplicates: {initial_duplicate_count} duplicate records found and removed")
print(f"  - Data Type Issues:")
print(f"    * total_spent stored as string with '$' and ',' symbols")
print(f"    * join_date and last_purchase had mixed date formats")
print(f"    * total_purchases and age stored as float instead of int")

# 9.2 Describe the changes made to standardize the dataset
# REQUIRED OUTPUT FORMAT:
# Standardization Changes:
# - Names: Converted to proper case
# - Categories: [describe standardization]
# - Phone Numbers: [describe format]
# Your code here
print("\nStandardization Changes:")
print(f"  - Names: Converted to proper case")
print(f"  - Categories: Standardized to title case")
print(f"  - Phone Numbers: Standardized to {phone_format} format")

# 9.3 Present key business insights from the cleaned data
# REQUIRED OUTPUT FORMAT:
# Key Business Insights:
# - Customer Base: X total customers
# - Revenue by Loyalty: [show averages]
# - Top Category: [category] with $X revenue
# Your code here
print("\nKey Business Insights:")
print(f"  - Customer Base: {len(df_final)} total customers")
print(f"\n  - Revenue by Loyalty:")
for status, avg in avg_spent_by_loyalty.sort_values(ascending=False).items():
    print(f"    * {status}: ${avg:.2f} average spend")
print(f"\n  - Top Category: {category_revenue.index[0]} with ${category_revenue.iloc[0]:.2f} revenue")

# 9.4 Display the first few rows of the clean, analysis-ready dataset
# REQUIRED: Display first 5 rows of 'df_final'
# Your code here
print(df_final.head().to_string())
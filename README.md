Improved Detection of Fraud Cases in E-commerce and Bank Transactions
Project Overview
This project aims to improve the detection of fraudulent activities in e-commerce and bank transactions by leveraging data preprocessing, exploratory data analysis (EDA), and feature engineering techniques. The project integrates data from various sources, including transaction data and geolocation data based on IP addresses, to enhance fraud detection models.

Table of Contents
Project Overview
Table of Contents
Installation
Usage
Data Preprocessing and Analysis
Exploratory Data Analysis (EDA)
Geolocation Analysis

Installation
Clone the repository:
git clone https://github.com/jealsab/Fraud-detection-in-e-commerce-and-bank-transactions.git
Navigate to the project directory:
cd Fraud-detection-in-e-commerce-and-bank-transactions
Install the required packages:
pip install -r requirements.txt
Usage
Place your raw data files (Fraud_Data.csv, creditcard.csv, IpAddress_to_Country.csv) in the data directory.
Run the main notebook or script to preprocess data, perform EDA, and merge datasets:
Data Preprocessing and Analysis
Handling Missing Values
Drop rows with missing values from Fraud_Data.csv.
Fill missing values in creditcard.csv with the mean of the respective columns.
Data Cleaning
Remove duplicate entries from both datasets.
Correct data types for numerical and categorical columns.
Normalization and Scaling
Normalize and scale purchase_value in Fraud_Data.csv.
Normalize and scale Amount in creditcard.csv.
Save Processed Data
Save the processed data into data/processed directory.
Exploratory Data Analysis (EDA)
Univariate Analysis
Histogram of purchase_value in Fraud_Data.csv.
Bivariate Analysis
Boxplot of purchase_value by class in Fraud_Data.csv.
Geolocation Analysis
Convert IP Addresses to Integer
Convert IP addresses in Fraud_Data.csv and IpAddress_to_Country.csv to integer format for efficient merging.
Merge Datasets
Merge Fraud_Data.csv with IpAddress_to_Country.csv based on IP address ranges to enrich fraud data with geolocation information.
Country Distribution
Visualize the distribution of countries in IpAddress_to_Country.csv.

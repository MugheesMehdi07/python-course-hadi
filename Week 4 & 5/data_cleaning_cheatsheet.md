# Data Cleaning Techniques Cheat Sheet

Data cleaning is a critical step in the data science workflow. It involves preparing data for analysis by fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. This cheat sheet provides an overview of common data cleaning techniques, what they are used for, and how to use them.

## Table of Contents

- [Handling Missing Values](#handling-missing-values)
- [Detecting and Removing Outliers](#detecting-and-removing-outliers)
- [Normalizing and Scaling Data](#normalizing-and-scaling-data)
- [Encoding Categorical Variables](#encoding-categorical-variables)
- [Dealing with Date and Time](#dealing-with-date-and-time)
- [Text Data Cleaning](#text-data-cleaning)
- [Duplicate Data](#duplicate-data)
- [Data Type Conversions](#data-type-conversions)
- [Splitting Columns](#splitting-columns)

## Handling Missing Values

- **Dropping**: Remove rows with missing values if the dataset is large enough and missing data is not significant.
  - `df.dropna()`
- **Imputation**: Replace missing values with statistical measures (mean, median, mode).
  - `df.fillna(df.mean())` for numerical columns
  - `df.fillna(df.mode()[0])` for categorical columns

## Detecting and Removing Outliers

- **Standard Deviation Method**: If data is normally distributed, remove data outside µ ± 3σ.
- **Interquartile Range (IQR) Method**: Remove data outside the 1.5 * IQR from the Q1 and Q3 quartiles.
  - `Q1 = df.quantile(0.25)`
  - `Q3 = df.quantile(0.75)`
  - `IQR = Q3 - Q1`
  - `df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]`

## Normalizing and Scaling Data

- **Normalization (Min-Max Scaling)**: Scale features to a range between 0 and 1.
  - `from sklearn.preprocessing import MinMaxScaler`
- **Standardization (Z-score Normalization)**: Scale features so they have the properties of a standard normal distribution with µ = 0 and σ = 1.
  - `from sklearn.preprocessing import StandardScaler`

## Encoding Categorical Variables

- **One-Hot Encoding**: Convert categorical variables into a form that could be provided to ML algorithms.
  - `pd.get_dummies(df)`
- **Label Encoding**: Convert each value in a column to a number.
  - `from sklearn.preprocessing import LabelEncoder`

## Dealing with Date and Time

- Convert string to datetime format: `pd.to_datetime(df['column_name'])`
- Extracting components: `df['year'] = df['date_column'].dt.year`

## Text Data Cleaning

- **Lowercasing**: Convert all letters to lowercase.
- **Removing Punctuation**: Remove all punctuation symbols.
- **Removing Stopwords**: Filter out common words that add little meaning.
  - `from nltk.corpus import stopwords`
- **Stemming/Lemmatization**: Reduce words to their base or root form.
  - `from nltk.stem import PorterStemmer`

## Duplicate Data

- Identify duplicate rows: `df.duplicated()`
- Remove duplicate rows: `df.drop_duplicates()`

## Data Type Conversions

- Convert data types: `df.astype({'column_name': 'new_type'})`

## Splitting Columns

- Splitting one column into multiple: `df['new_col1'], df['new_col2'] = zip(*df['original_col'].str.split(' '))`

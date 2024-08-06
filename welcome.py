import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/kaggle/input/world-languages-dataset/languages_dataset.csv"
df_languages = pd.read_csv(file_path)

# Display the first few rows of the dataset
df_languages.head()

# Display information about the dataset
df_languages.info()

# Display statistical summary for numerical columns
df_languages.describe()

# Check for missing values
missing_values = df_languages.isnull().sum()
missing_values

# Convert columns to appropriate data types if necessary
df_languages['Speakers'] = df_languages['Speakers'].astype(int)

# Verify the changes
df_languages.dtypes

# Plot the distribution of languages by family
plt.figure(figsize=(10, 6))
sns.countplot(y='Family', data=df_languages, order=df_languages['Family'].value_counts().index)
plt.title('Distribution of Languages by Family')
plt.xlabel('Number of Languages')
plt.ylabel('Language Family')
plt.show()

# Plot the distribution of languages by region
plt.figure(figsize=(10, 6))
sns.countplot(y='Region', data=df_languages, order=df_languages['Region'].value_counts().index)
plt.title('Distribution of Languages by Region')
plt.xlabel('Number of Languages')
plt.ylabel('Region')
plt.show()

# Plot the top 10 languages by number of speakers
top_languages = df_languages.nlargest(10, 'Speakers')
plt.figure(figsize=(10, 6))
sns.barplot(x='Speakers', y='Language', data=top_languages, palette='viridis')
plt.title('Top 10 Languages by Number of Speakers')
plt.xlabel('Number of Speakers')
plt.ylabel('Language')
plt.show()

# Plot the distribution of writing systems
plt.figure(figsize=(10, 6))
sns.countplot(y='Writing System', data=df_languages, order=df_languages['Writing System'].value_counts().index)
plt.title('Distribution of Writing Systems')
plt.xlabel('Number of Languages')
plt.ylabel('Writing System')
plt.show()

# Plot the relationship between language families and number of speakers
plt.figure(figsize=(12, 6))
sns.boxplot(x='Family', y='Speakers', data=df_languages)
plt.title('Number of Speakers across Different Language Families')
plt.xlabel('Language Family')
plt.ylabel('Number of Speakers')
plt.xticks(rotation=45)
plt.show()

# Plot the relationship between regions and writing systems
plt.figure(figsize=(12, 6))
sns.countplot(x='Region', hue='Writing System', data=df_languages)
plt.title('Writing Systems Used in Different Regions')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot pairplot of numerical features
sns.pairplot(df_languages[['Speakers']])
plt.suptitle('Pairplot of Numerical Features', y=1.02)
plt.show()

# Plot the count of languages by region and family
plt.figure(figsize=(14, 8))
sns.countplot(x='Region', hue='Family', data=df_languages)
plt.title('Languages Distribution by Region and Family')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Family', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Plot a pie chart of writing systems
plt.figure(figsize=(8, 8))
df_languages['Writing System'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set3')
plt.title('Distribution of Writing Systems')
plt.ylabel('')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/Internship_job_listings_with_skills.csv'
df = pd.read_csv(file_path)

# Print the DataFrame to check its structure
print(df.head())
print("\nColumn Names:", df.columns)  # Print the column names

# Perform basic EDA
print("\nBasic Information:")
print(df.info())

# Visualize job titles
plt.figure(figsize=(10, 6))
sns.countplot(y='Title', data=df, order=df['Title'].value_counts().index)
plt.title('Job Title Distribution')
plt.xlabel('Count')
plt.ylabel('Job Title')
plt.show()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

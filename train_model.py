import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
df = pd.read_csv('data/Internship_job_listings_with_skills.csv')

# Prepare your data
X = df[['Title', 'Address', 'On which Day Job Uploaded', 'Level', 'required_skills']]
y = df['Level']  # Assuming 'Level' is your target variable

# Convert categorical data to numerical using one-hot encoding
X = pd.get_dummies(X, columns=['Title', 'Address', 'On which Day Job Uploaded', 'Level', 'required_skills'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
model_path = 'models/job_model.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")

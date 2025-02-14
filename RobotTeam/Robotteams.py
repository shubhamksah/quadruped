import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("match_data.csv")  # Your structured data

# Define features (X) and target variable (y)
X = data[['Avg Score 1', 'Avg Score 2', 'Avg Score 3', 'Avg Score 4']]
y = data['Winner(s)']  # Categorical outcome (teams that won)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

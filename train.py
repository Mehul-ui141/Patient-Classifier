import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

# Fake hospital-like data (simple but matching your UI)
X = np.array([
    [37, 95, 120, 15],
    [39, 85, 90, 5],
    [36.5, 98, 110, 18],
    [35, 80, 70, 2],
    [38, 88, 100, 10],
    [37, 97, 130, 16]
])

# 1 = Sent Home, 0 = Keep
y = np.array([1, 0, 1, 0, 0, 1])

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("✅ Model saved!")
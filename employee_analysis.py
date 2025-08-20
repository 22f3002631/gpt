# employee_analysis.py
# Email: 22f3002631@ds.study.iitm.ac.in
# Business Case: Employee Performance Analysis

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load dataset
# -----------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,North America,79.25,1,4.4
EMP002,IT,Asia Pacific,76.04,6,3.2
EMP003,IT,Latin America,80.58,11,3.3
EMP004,Marketing,Asia Pacific,66.68,6,4.9
EMP005,IT,North America,90.94,4,3
EMP006,Finance,Europe,82.14,8,4.2
EMP007,HR,North America,70.25,3,4.0
EMP008,IT,Asia Pacific,85.60,7,3.5
EMP009,Finance,Latin America,78.40,9,3.7
EMP010,Marketing,Europe,88.20,5,4.1
"""
from io import StringIO
df = pd.read_csv(StringIO(data))

# -----------------------------
# Step 2: Frequency count for IT department
# -----------------------------
it_count = df[df["department"] == "IT"].shape[0]
print(f"Frequency count for IT department: {it_count}")

# -----------------------------
# Step 3: Create histogram
# -----------------------------
plt.figure(figsize=(6, 6))
df["department"].value_counts().plot(kind="bar", color=["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"])

plt.title("Employee Count by Department", fontsize=14, pad=15)
plt.xlabel("Department")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("histogram.png")

# -----------------------------
# Step 4: Export as HTML file
# -----------------------------
html_content = f"""
<html>
<head>
    <title>Employee Performance Analysis</title>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <p><strong>Email:</strong> 22f3002631@ds.study.iitm.ac.in</p>
    <p>Frequency count for IT department: {it_count}</p>
    <h2>Histogram of Departments</h2>
    <img src="histogram.png" alt="Histogram" width="500">
</body>
</html>
"""

with open("employee_analysis.html", "w", encoding="utf-8") as f:
    f.write(html_content)

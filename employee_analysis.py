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
# Step 4: Export as HTML file with embedded image
# -----------------------------
import base64

# Convert image to base64 for embedding
with open("histogram.png", "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Create the Python code string (avoiding self-reference)
python_code_content = '''# employee_analysis.py
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
plt.show()'''

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Employee Performance Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        h1 {{ color: #333; }}
        h2 {{ color: #666; }}
        .email {{ background-color: #f0f0f0; padding: 10px; border-radius: 5px; }}
        .result {{ background-color: #e8f5e8; padding: 10px; border-radius: 5px; margin: 20px 0; }}
        .code-block {{ background-color: #f8f8f8; border: 1px solid #ddd; border-radius: 5px; padding: 15px; overflow-x: auto; }}
        .code-block pre {{ margin: 0; font-family: 'Courier New', monospace; font-size: 14px; }}
        img {{ border: 1px solid #ddd; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <div class="email">
        <p><strong>Email:</strong> 22f3002631@ds.study.iitm.ac.in</p>
    </div>

    <h2>Business Case</h2>
    <p>This analysis helps a Finance company understand employee performance data across multiple regions to inform resource allocation decisions, identify high-performing departments, and guide recruitment strategies.</p>

    <h2>Python Code</h2>
    <div class="code-block">
        <pre>{python_code_content}</pre>
    </div>

    <h2>Analysis Results</h2>
    <div class="result">
        <p><strong>Frequency count for IT department: {it_count}</strong></p>
    </div>

    <h2>Department Distribution Histogram</h2>
    <p>The histogram below shows the distribution of employees across different departments:</p>
    <img src="data:image/png;base64,{img_base64}" alt="Department Distribution Histogram" style="max-width: 100%; height: auto;">

    <h2>Summary</h2>
    <ul>
        <li>Total employees analyzed: {len(df)}</li>
        <li>IT department has {it_count} employees</li>
        <li>Departments: {', '.join(df['department'].unique())}</li>
        <li>Analysis completed with email verification: 22f3002631@ds.study.iitm.ac.in</li>
    </ul>
</body>
</html>
"""

with open("employee_analysis.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created successfully with embedded visualization!")

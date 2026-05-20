import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/students.csv")

# Display first few rows
print(df.head())

# Statistical summary
print(df.describe())

# Calculate average score
df['average'] = df[['math', 'science', 'english']].mean(axis=1)

# Plot distribution of average scores
plt.figure()
plt.hist(df['average'])
plt.title("Average Score Distribution")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.show()

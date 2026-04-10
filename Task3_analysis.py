# Task3 Analysis
import pandas as pd
import numpy as np
import os

# Loading of the file 
csv_file = "data/trends_clean.csv"
df = pd.read_csv(csv_file)

print(f"Loaded data: {df.shape}")   # rows and columns
print("\nFirst 5 rows:")
print(df.head())

# Average score and comments
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print(f"\nAverage score   : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# Utilization of NumPy 
scores = df["score"].values

print("\n--- NumPy Stats ---")
print(f"Mean score   : {np.mean(scores):.2f}")
print(f"Median score : {np.median(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

# Category with most stories present
most_category = df["category"].value_counts().idxmax()
most_count = df["category"].value_counts().max()
print(f"\nMost stories in: {most_category} ({most_count} stories)")

#  most commented story
max_comments_idx = df["num_comments"].idxmax()
max_story = df.loc[max_comments_idx]
print(f"\nMost commented story: \"{max_story['title']}\"  — {max_story['num_comments']} comments")

# Adding New Columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Saving the Result as .csv file
os.makedirs("data", exist_ok=True)
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}") #output file name print
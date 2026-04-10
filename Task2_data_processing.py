# Task 2 Processing Data
import pandas as pd
import os
from datetime import datetime

# Loading the JSON file created
# Use of today's date to match the file created in Task 1
date_str = datetime.now().strftime("%Y%m%d")
json_file = f"data/trends_{date_str}.json"

# DataFrame creation
df = pd.read_json(json_file)
print(f"Loaded {len(df)} stories from {json_file}")

# Data Cleaning
# Removing duplicates by post_id
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Dropping rows with missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# confiming score and num_comments are integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Removal of low quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Stripping extra spaces from title
df["title"] = df["title"].str.strip()

# Save the file as CSV
os.makedirs("data", exist_ok=True)
csv_file = "data/trends_clean.csv"
df.to_csv(csv_file, index=False)

print(f"Saved {len(df)} rows to {csv_file}")

# Print of how many stories per category
print("\nStories per category:")
print(df["category"].value_counts())
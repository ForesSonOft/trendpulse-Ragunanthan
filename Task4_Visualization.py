# Task 4 Visualization
import pandas as pd
import matplotlib.pyplot as plt
import os

# Setup the file
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it doesn't exist i.e making sure
os.makedirs("outputs", exist_ok=True)

# Chart 1: Top 10 Stories by Score
top10 = df.nlargest(10, "score").copy()
# Shorten titles longer than 50 characters
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(8, 6))
plt.barh(top10["short_title"], top10["score"], color="skyblue")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# Chart 2: Stories per Category
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 6))
category_counts.plot(kind="bar", color=["red", "green", "blue", "orange", "purple"])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# Chart 3: Score vs Comments Scatter Plot
plt.figure(figsize=(8, 6))
colors = df["is_popular"].map({True: "blue", False: "gray"})
plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend(["Popular", "Not Popular"])
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# Bonus — Dashboard.png with all 3 charts
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"], color="skyblue")
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values, color=["red", "green", "blue", "orange", "purple"])
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

# Chart 3 in dashboard
axes[2].scatter(df["score"], df["num_comments"], c=colors, alpha=0.7)
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")

fig.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("Charts saved in outputs/:")
print(" - chart1_top_stories.png")
print(" - chart2_categories.png")
print(" - chart3_scatter.png")
print(" - dashboard.png")
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

input_file = Path("data/trends_analysed.csv")
output_folder = Path("outputs")

# Create outputs folder if it does not exist
output_folder.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(input_file)

top_stories = df.nlargest(10, "score").copy()

# Shorten long titles
top_stories["short_title"] = top_stories["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

plt.figure(figsize=(10, 6))
plt.barh(top_stories["short_title"], top_stories["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig(output_folder / "chart1_top_stories.png")
plt.close()

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(output_folder / "chart2_categories.png")
plt.close()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 6))
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
plt.scatter(popular["score"], popular["num_comments"], label="Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()

plt.savefig(output_folder / "chart3_scatter.png")
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Dashboard Chart 1
axes[0].barh(top_stories["short_title"], top_stories["score"])
axes[0].set_title("Top Stories")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")
axes[0].invert_yaxis()

# Dashboard Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=30)

# Dashboard Chart 3
axes[2].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)
axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

fig.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout()

plt.savefig(output_folder / "dashboard.png")
plt.close()

print("All charts saved successfully in outputs/")

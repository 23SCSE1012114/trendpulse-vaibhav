import pandas as pd
import numpy as np
from pathlib import Path

input_file = Path("data/trends_clean.csv")
output_file = Path("data/trends_analysed.csv")

df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Average score and comments
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

max_score = np.max(scores)
min_score = np.min(scores)

# Category with most stories
top_category = df["category"].value_counts().idxmax()
top_category_count = df["category"].value_counts().max()

# Story with most comments
max_comment_index = np.argmax(comments)
most_commented_title = df.loc[max_comment_index, "title"]
most_comments = df.loc[max_comment_index, "num_comments"]

print("\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score:.2f}")
print(f"Median score : {median_score:.2f}")
print(f"Std deviation: {std_score:.2f}")
print(f"Max score    : {max_score}")
print(f"Min score    : {min_score}")

print(f"\nMost stories in: {top_category} ({top_category_count} stories)")

print(
    f'\nMost commented story: "{most_commented_title}" '
    f'— {most_comments} comments'
)

# Engagement = comments per score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular if score > average score
df["is_popular"] = df["score"] > avg_score

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")

import pandas as pd
from pathlib import Path


# File paths
input_file = Path("data/trends_20240115.json")   # change date if needed
output_file = Path("data/trends_clean.csv")

df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# Remove duplicate rows based on post_id
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing important values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Strip extra spaces from title
df["title"] = df["title"].astype(str).str.strip()

# Convert score and num_comments to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)

# Remove low-quality stories
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Print stories per category
print("\nStories per category:")
print(df["category"].value_counts())

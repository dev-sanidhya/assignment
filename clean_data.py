import pandas as pd

# Load original data
df = pd.read_csv("event_data.csv")

# Clean name fields
if "first_name" not in df.columns or "last_name" not in df.columns:
    df[["first_name", "last_name"]] = df["name"].str.extract(r"^(\S+)\s+(.*)$")

# Replace missing values safely
df["first_name"] = df["first_name"].fillna("")
df["last_name"] = df["last_name"].fillna("")
df["name"] = df["name"].fillna(df["first_name"] + " " + df["last_name"])
df["Job Title"] = df["Job Title"].fillna("Not Provided")

# LinkedIn column
linkedin_col = "What is your LinkedIn profile?"
df[linkedin_col] = df[linkedin_col].fillna("")
df["linkedin_missing"] = ~df[linkedin_col].astype(str).str.startswith("http")

# Save cleaned data
df.to_csv("cleaned_event_data.csv", index=False)

# Save LinkedIn issues for manual review
df[df["linkedin_missing"]].to_csv("linkedin_review.csv", index=False)

# Save a simple summary report
with open("summary.txt", "w") as f:
    f.write(f"Total rows: {len(df)}\n")
    f.write(f"Missing/Invalid LinkedIn profiles: {df['linkedin_missing'].sum()}\n")
    f.write(f"Unique Job Titles: {df['Job Title'].nunique()}\n")
    f.write(f"Rows needing manual LinkedIn review: {len(df[df['linkedin_missing']])}\n")

import pandas as pd
import os
import re

def generate_message(row):
    name = row.get("first_name") or row.get("name", "").split()[0]
    job = str(row.get("Job Title", "")).strip()
    joined = str(row.get("has_joined_event", "")).strip().lower() in ["yes", "true"]
    linkedin = str(row.get("What is your LinkedIn profile?", "")).strip()

    if joined:
        return f"Hey {name}, thanks for joining our session! As a {job.lower() if job else 'professional'}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        return f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job.lower() if job else 'professional'}."

def sanitize_filename(email):
    return re.sub(r'[^a-zA-Z0-9]', '_', email)

def main():
    input_file = "cleaned_event_data.csv"
    output_csv = "personalized_messages.csv"
    output_txt_dir = "messages_txt"

    os.makedirs(output_txt_dir, exist_ok=True)

    df = pd.read_csv(input_file)
    df["has_joined_event"] = df["has_joined_event"].astype(str).str.strip().str.lower().map({"yes": True, "no": False, "true": True, "false": False})
    df["Job Title"] = df["Job Title"].fillna("").astype(str)
    df["What is your LinkedIn profile?"] = df["What is your LinkedIn profile?"].fillna("").astype(str)

    df["message"] = df.apply(generate_message, axis=1)
    df[["email", "message"]].to_csv(output_csv, index=False)

    for _, row in df.iterrows():
        raw_email = row["email"]
        if pd.isna(raw_email) or not raw_email.strip():
            continue
        filename = sanitize_filename(raw_email) + ".txt"
        filepath = os.path.join(output_txt_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(row["message"])

if __name__ == "__main__":
    main()
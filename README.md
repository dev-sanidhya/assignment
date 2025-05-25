# Event Data Cleaning Assignment

## ✅ Objective

Clean and process messy event registration data, identify incomplete entries, and output cleaned files for further use. Additionally, generate auto-personalized messages based on user data.

---

## 📄 Files Included

| File                      | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| clean_data.py             | Script that cleans and processes `event_data.csv`              |
| event_data.csv            | Original raw dataset                                           |
| cleaned_event_data.csv    | Fully cleaned version of the data                              |
| linkedin_review.csv       | Subset of rows with missing or invalid LinkedIn profile URLs   |
| summary.txt               | Quick summary report of the cleanup                            |
| auto_message.py           | Script to generate personalized messages based on cleaned data |
| personalized_messages.csv | CSV output of emails and their customized messages             |
| messages_txt/             | Folder containing one `.txt` file per user with their message  |

---

## ⚙ How to Run

### Step 1: Data Cleaning

Make sure you have Python 3 and pandas installed.

```bash
python clean_data.py
```

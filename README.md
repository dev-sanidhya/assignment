# How to Run

## Step 1: Data Cleaning

### Prerequisite

Make sure you have Python 3 and pandas installed.

### Command

```bash
python clean_data.py
```

Output Files Generated
cleaned_event_data.csv

linkedin_review.csv

summary.txt

Step 2: Auto-Personalized Messaging
Note: Run this only after completing Step 1.

Command
bash
python auto_message.py
Output Files Generated
personalized_messages.csv (CSV with email and message columns)

messages_txt/ (folder with individual .txt files for each user)

Bonus
The messaging script automatically saves individual message files in the messages_txt/ folder.

Requirements
Python 3.x

pandas (pip install pandas)

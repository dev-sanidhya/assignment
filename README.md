# Event Data Cleaning Assignment

## ✅ Objective

Clean and process messy event registration data, identify incomplete entries, and output cleaned files for further use. Additionally, generate auto-personalized messages based on user data.

---

## 📄 Files Included

| File                        | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| `clean_data.py`             | Script that cleans and processes `event_data.csv`              |
| `event_data.csv`            | Original raw dataset                                           |
| `cleaned_event_data.csv`    | Fully cleaned version of the data                              |
| `linkedin_review.csv`       | Subset of rows with missing or invalid LinkedIn profile URLs   |
| `summary.txt`               | Quick summary report of the cleanup                            |
| `auto_message.py`           | Script to generate personalized messages based on cleaned data |
| `personalized_messages.csv` | CSV output of emails and their customized messages             |
| `messages_txt/`             | Folder containing one `.txt` file per user with their message  |

---

# 🚀 How to Run

## 🔧 Step 1: Data Cleaning

### 📋 Prerequisite

> Make sure you have Python 3 and pandas installed.

### ⌨️ Command

```bash
python clean_data.py
```

📂 Output Files Generated

📄 cleaned_event_data.csv  
🔗 linkedin_review.csv  
📝 summary.txt

## 🔧 Step 2: Generate Personalized Messages

Note: Run this only after completing step 1.

### ⌨️ Command

```bash
python auto_message.py
```

📂 Output Files Generated

💌 personalized_messages.csv (CSV with email/message columns)  
📁 messages_txt/ (individual .txt files for each user)

## <h3 style="font-size: 1.25em">🎁 Bonus</h3>

The messaging script automatically saves individual message files in the `messages_txt/` folder.

## <h3 style="font-size: 1.25em">⚙️ Requirements</h3>

🐍 Python 3.x  
📦 pandas (install via `pip install pandas`)

# 🧠 Spam Detection using Naive Bayes

This project implements a **Spam Email Classifier** using the **Naive Bayes algorithm** from scratch in Python. It classifies emails as either **Spam** or **Ham (Not Spam)** based on word probabilities.

---

## 📌 Project Features

- Preprocessing of raw email text  
- Word frequency and likelihood calculation  
- Implementation of Naive Bayes Classifier  
- Evaluation using sample emails  
- Built without external ML libraries (pure Python)

---

## 📁 Folder Structure

spam_detection_naive_bayes/
│
├── spam_classifier.py # Naive Bayes logic
├── preprocess.py # Email preprocessing functions
├── sample_emails.csv # Example dataset (spam & ham emails)
├── test_script.py # Test script to run predictions
├── README.md # Project documentation
└── requirements.txt # Required Python packages


---

## 🧮 How It Works

1. **Preprocess Emails**: Remove punctuation, stopwords, and lowercase all words.
2. **Word Frequency**: Count word frequency for each class (Spam and Ham).
3. **Probability Calculation**: Use Bayes' Theorem to calculate probabilities.
4. **Prediction**: Classify based on which class has the highest likelihood.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/dnikhilaaa/spam_detection_naive_bayes.git
cd spam_detection_naive_bayes

2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Classifier
bash
Copy
Edit
python test_script.py
📊 Sample Output
vbnet
Copy
Edit
Email: "Get free coupons now!"
Prediction: Spam

Email: "Meeting scheduled at 10 AM"
Prediction: Ham
🔍 Project Goals
Understand the inner working of Naive Bayes

Learn how to preprocess unstructured text

Build an end-to-end mini classifier from scratch

🛠️ Tech Stack
Python

NumPy

Pandas (for dataset handling)

Text preprocessing (manual & regex-based)

🤝 Acknowledgements
Inspired by classic spam detection problems and academic exercises in NLP.

📬 Contact
Nikhila Reddy
📧 nikhila.reddy@example.com
🔗 LinkedIn
🐙 GitHub


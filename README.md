# 📩 Spam Message Detection using Machine Learning

This project uses Natural Language Processing (NLP) and machine learning to classify SMS messages as **Spam** or **Ham (Not Spam)**. It leverages text cleaning, feature extraction (TF-IDF), and a Naive Bayes classifier to achieve high accuracy.

---

## 📌 Problem Statement

SMS spam is a common issue that clutters inboxes and wastes user time. The goal is to build a model that can **automatically detect spam messages** using historical labeled data.

---

## 🧠 Approach

1. **Text Preprocessing**
   - Lowercasing, punctuation removal, stopword removal, stemming

2. **Feature Extraction**
   - TF-IDF Vectorizer to convert text into numerical features

3. **Model Building**
   - Multinomial Naive Bayes classifier

4. **Evaluation**
   - Accuracy, Confusion Matrix, Precision, Recall, F1 Score

---

## 📊 Results

| Metric      | Score     |
|-------------|-----------|
| Accuracy    | 98.6%     |
| Precision   | 97.9%     |
| Recall      | 98.3%     |
| F1 Score    | 98.1%     |

> ✅ Model performs well on both spam and ham classification with minimal false positives.

---

## 📁 Dataset

- Source: [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- 5,572 SMS messages labeled as spam or ham

---

## 🚀 How to Run

```bash
git clone https://github.com/dnikhilaaa/spam-detection.git
cd spam-detection
pip install -r requirements.txt
python spam_classifier.py


✍️ Author
Nikhila
🎓 MBA in Analytics and Data Science
🔗 GitHub Profile

📬 Contact
Have any suggestions or questions?
📧 nikhilareddy1605@gmail.com | LinkedIn (linkedin.com/in/nikhila-reddy-923588257/)


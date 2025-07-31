import re
from collections import defaultdict
import math

def preprocess_email(email):
    email = email.lower()
    email = re.sub(r"[^a-z\s]", "", email)
    return email.split()

def get_word_frequency(emails, labels):
    word_frequency = {
        'spam': defaultdict(int),
        'ham': defaultdict(int)
    }

    class_count = {
        'spam': 0,
        'ham': 0
    }

    for i, email in enumerate(emails):
        label = labels[i]
        words = preprocess_email(email)
        class_count[label] += 1
        for word in words:
            word_frequency[label][word] += 1

    return word_frequency, class_count

def prob_word_given_class(word, label, word_frequency, class_count):
    word_count = sum(word_frequency[label].values())
    return (word_frequency[label][word] + 1) / (word_count + len(word_frequency[label]))

def prob_email_given_class(email, label, word_frequency, class_count):
    words = preprocess_email(email)
    prob = math.log(class_count[label] / sum(class_count.values()))
    for word in words:
        prob += math.log(prob_word_given_class(word, label, word_frequency, class_count))
    return prob

def naive_bayes(email, word_frequency, class_count):
    spam_prob = prob_email_given_class(email, 'spam', word_frequency, class_count)
    ham_prob = prob_email_given_class(email, 'ham', word_frequency, class_count)
    return 1 if spam_prob > ham_prob else 0  # 1 = spam, 0 = ham

# Example usage:
emails = [
    "Congratulations! You've won a free lottery ticket.",
    "Meeting tomorrow at 10am",
    "You are selected for a cash prize, claim now!",
    "Please find the attached agenda for today’s meeting."
]
labels = ['spam', 'ham', 'spam', 'ham']

word_frequency, class_count = get_word_frequency(emails, labels)
new_email = "Win a free cash prize now!"
result = naive_bayes(new_email, word_frequency, class_count)
print("Spam" if result == 1 else "Ham")

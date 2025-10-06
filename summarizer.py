# Document Summarizer using Frequency Method
from collections import Counter

def summarize(text):
    words = text.split()
    freq = Counter(words)
    most_common = freq.most_common(5)
    summary = ' '.join([w for w, _ in most_common])
    return summary

if __name__ == "__main__":
    text = input("Enter text: ")
    print("Summary:", summarize(text))

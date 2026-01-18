import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download("punkt")
nltk.download("stopwords")

def summarize_text(text, num_sentences=5):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w.isalnum() and w not in stop_words]

    word_freq = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return " ".join(summary[:num_sentences])

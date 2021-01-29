import yargy
import nltk
import sys
import wordcloud
from collections import defaultdict as dd
from operator import itemgetter
from nltk import word_tokenize
from nltk.corpus import stopwords
from rusenttokenize import ru_sent_tokenize
import string
import logging
import pymorphy2
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

logging.getLogger().setLevel(logging.ERROR)

morph_analyzer = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words('russian')

def show_wordcloud_by_freq_dict(freq_dict):
    wordcloud = WordCloud()
    wordcloud.generate_from_frequencies(frequencies=freq_dict)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def preprocess_tokenize(text):
    text_preprocessed_tokenized = []

    for sentence in ru_sent_tokenize(text):
        clean_words = [word.strip(string.punctuation) for word in word_tokenize(text)]
        clean_words = [word for word in clean_words if word]
        clean_words = [word.lower() for word in clean_words if word]
        clean_words = [word for word in clean_words if word not in russian_stopwords]

        clean_lemmas = [morph_analyzer.parse(word)[0].normal_form for word in clean_words]

        text_preprocessed_tokenized.extend(clean_lemmas)

    return text_preprocessed_tokenized

corpus = []
with open('texts/Том 2.txt', 'r', encoding='utf-8') as corpus_f:
    for document in corpus_f:
        corpus.append(document)
        # if len(corpus) > 1000:
        #      break


tfidf_vectorizer = TfidfVectorizer(tokenizer=preprocess_tokenize)
tfidf_vectorizer.fit_transform(corpus)
feature_names = tfidf_vectorizer.get_feature_names()

str1 = ' '.join(str(e) for e in corpus)
#for document in corpus:
X = tfidf_vectorizer.transform([str1])

tfidf_scores = [(feature_names[col], X[0, col]) for col in X.nonzero()[1]]
freq_list = [(word, freq) for word, freq in sorted(tfidf_scores,
                                                       key=itemgetter(1),
                                                       reverse=True)]

show_wordcloud_by_freq_dict(dict(freq_list))

f = open("Results/Tom2_dict.txt","w", encoding="utf-8")
f.write(str(dict(freq_list)))
f.close()

print(document)

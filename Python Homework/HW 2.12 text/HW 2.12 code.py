import string
from gensim.utils import tokenize
from gensim.summarization.textcleaner import split_sentences
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from pymorphy2 import MorphAnalyzer
from string import punctuation
import re, os, json
morph = MorphAnalyzer()
my_file = open('city_smells.txt', 'r', encoding='utf-8')
read_file = my_file.read()
my_file.close()
read_file_normalized = read_file.translate(str.maketrans('','',string.punctuation))
lower_case_file = read_file_normalized.lower()
sent_list = sent_tokenize(read_file, 'russian')
words = list(tokenize(read_file_normalized, lowercase= True))
result = open("HW 2.12 results.txt", 'w', encoding='utf-8')
result.write('Результаты анализа текста City smells'+ '\n')
average_word = str(sum(len(word) for word in words) / len(words))
result.write('1. Средняя длина слова в тексте City smells = ' + average_word + ' знаков' + '\n')
average_sent = str(sum(len(_) for _ in sent_list) / len(sent_list))
result.write('2. Средняя длина предложения в тексте City smells = ' + average_sent + ' знаков' + '\n')
result.close()

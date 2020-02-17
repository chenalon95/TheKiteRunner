# coding=utf-8
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/home/chen/הורדות/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/home/chen/הורדות/stanford-ner-2018-10-16/stanford-ner.jar',
                       encoding='utf-8')
x = 'Hi my name is Chen'
tokenized_text = word_tokenize(x)
classified_text = st.tag(tokenized_text)
print(classified_text)

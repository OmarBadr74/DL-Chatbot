from nltk.tokenize import PunktSentenceTokenizer
EXAMPLE_TEXT = 'Hi, how are you! i wish you have a good day.I am omar? do you know me , hhhhhhh lol.'
custom_sent_tokenizer = PunktSentenceTokenizer(EXAMPLE_TEXT)
tokenized = custom_sent_tokenizer.tokenize(EXAMPLE_TEXT)
tokenized[:10]
print('custom_sent_tokenizer:',custom_sent_tokenizer)
print('tokenized:',tokenized)
from nltk.tokenize import sent_tokenize
for s in sent_tokenize(EXAMPLE_TEXT) :
        print(s)
        print('----------------------')
        
import nltk
sen = nltk.sent_tokenize(EXAMPLE_TEXT)
print(sen)
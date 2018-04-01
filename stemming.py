from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

text = "I enjoy riding, I rode the bike. It was very helpful"

words  = word_tokenize(text) 

for i in words:
	print(ps.stem(i))
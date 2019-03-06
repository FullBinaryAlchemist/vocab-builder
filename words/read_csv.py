import csv
import os
from study.models import WordList
def init_database():
	with open(os.path.abspath('words\\wordlist.csv'),'rt') as words_file:
		words = csv.reader(words_file,delimiter=",")
		next(words,None)
		for word_row in words:
			WordList.objects.create(word=word_row[0],definition=word_row[1].rstrip(),word_id=word_row[4])

			
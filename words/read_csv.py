import csv
import os
from study.models import List


def init_database():
	with open(os.path.abspath('words\\wordlist.csv'), 'rt') as words_file:
		words = csv.reader(words_file,delimiter=",")
		next(words,None)
		for word_row in words:
			if word_row[3]=="GRE":
				List.objects.create(list_type="GRE")
			else:
				List.objects.create(list_type="SAT")
			# WordList.objects.create(word=word_row[0],definition=word_row[1].rstrip(),word_id=word_row[4])


from django.conf import settings
from django.db import models
from django.utils import timezone


class Test(models.Model):
	test_id=models.IntegerField(default=1)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	word_id= models.ForeignKey(WordList,on_delete=models.CASCADE)

	#Assigns an id to the test
	def create_test_id(self):
		return self.test_id+1

	
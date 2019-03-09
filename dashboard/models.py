from django.db import models
from study.models import *

class TestsData(models.Model):
	test_id=models.IntegerField(default=1)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	word_id= models.ForeignKey(WordList,on_delete=models.CASCADE)
	right= models.BooleanField(default=False)
	
	class Meta:
		managed=True
		#	db_table='study_testdata'

class Tests(models.Model):
	test_data=models.ForeignKey(TestsData, on_delete=models.CASCADE)
	test_date= models.DateTimeField(default=timezone.now)
	
	class Meta:
		managed=True
		#db_table="study_test"

	def getscore(self):
		return self.test_data.objects.filter(right=True).count()


# Create your models here.

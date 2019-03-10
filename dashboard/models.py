from django.db import models
from study.models import *

class TestsData(models.Model):
	test_id=models.IntegerField(default=1)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	word_id= models.ForeignKey(WordList,on_delete=models.CASCADE)
	right= models.BooleanField(default=False)
	def __str__(self):
		return str((self.test_id,self.user,self.word_id,self.right))

	class Meta:
		managed=True
		#	db_table='study_testdata'

class Tests(models.Model):
	test_data=models.ForeignKey(TestsData, on_delete=models.CASCADE)
	test_date= models.DateTimeField(default=timezone.now)
	
	class Meta:
		managed=True
		#db_table="study_test"
	def __str__(self):
		return str((self.test_data.test_id,self.test_date, self.test_data.user))
	def getscore(self):
		return TestsData.objects.filter(models.Q(right=True) & models.Q(user=self.test_data.user) & models.Q(test_id=self.test_data.test_id)).count()
# Create your models here.

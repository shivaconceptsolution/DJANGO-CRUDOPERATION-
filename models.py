from django.db import models
class Student(models.Model):
	rno = models.IntegerField()
	sname = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)
	fees = models.IntegerField()
	def __str__(self):
		return "rno "+str(self.rno)+" sname "+self.sname +" branch "+self.branch+ " fees "+str(self.fees)

from django.db import models
from . import choices

class Department(models.Model):	
	class Meta:
		verbose_name_plural = 'Department'
	dept_id = models.AutoField(primary_key=True)
	dept_name = models.CharField(max_length=200)

	def __str__(self):
		return '%s' % (self.dept_name)


class Level(models.Model):
	class Meta:
		verbose_name_plural ='Level'
	level_id = models.AutoField(primary_key=True)
	level_name = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.level_name)


class Program(models.Model):
	program_id = models.AutoField(primary_key=True)
	program_name = models.CharField(max_length=200)
	program_short_name = models.CharField(max_length=30,null=True)
	dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)
	level = models.ForeignKey('Level', on_delete =models.CASCADE)

	def __str__(self):
		return '%s' % (self.program_name)


class Subject(models.Model):
	Subject_code = models.CharField(max_length=25)
	subject_type = models.CharField(choices = choices.SUBJECT_TYPE_CHOICES,max_length=20, default = 'COMPULSORY')#help_text='Compulsory')   #compulsory or elective
	subject_name = models.CharField(max_length=100)
	credit = models.IntegerField(null=True, blank=True)
	internal = models.IntegerField(null=True, blank=True)
	external = models.IntegerField(null=True, blank=True)
	total = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return '%s ' % (self.subject_name)

	

class Syllabus(models.Model):
	class Meta:
		verbose_name_plural = 'Syllabus'
	syllabus_id = models.AutoField(primary_key=True)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	syllabus_name = models.CharField(max_length=50,  help_text='BCT_I_I_Part')
	year = models.IntegerField()
	part = models.IntegerField()
	Subject = models.ManyToManyField(Subject)

	total_final_marks = models.IntegerField()

	def __str__(self):
		return '%s ' % (str(self.syllabus_name))







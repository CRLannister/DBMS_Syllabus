from django.db import models

# Create your models here.
class Department(models.Model):
	
	class Meta:
		verbose_name_plural = 'Department'
	

	dept_id = models.AutoField(primary_key=True)
	dept_name = models.CharField(max_length=200)

	def __str__(self):
		return '%s' % (self.dept_name)




class Program(models.Model):
	program_id = models.AutoField(primary_key=True)
	program_name = models.CharField(max_length=200)
	dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)
	# syllabus_id = 

	def __str__(self):
		return '%s' % (self.program_name)





class Syllabus(models.Model):
	
	class Meta:
		verbose_name_plural = 'Syllabus'


	syllabus_id = models.AutoField(primary_key=True)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	syllabus_name = models.CharField(max_length=50,  help_text='BCT_I_I_Part')
	# syllabus_code = models.CharField(max_length=40)
	year = models.IntegerField()
	part = models.IntegerField()
	#total_lecture_hr = models.DecimalField(max_digits=2,decimal_places=1)
	#total_tutorial_hr = models.DecimalField(max_digits=2,decimal_places=1)
	#total_practical_hr = models.DecimalField(max_digits=2,decimal_places=1)
	#total_theory_assessment_marks = models.IntegerField()
	#total_practical_assessment_marks = models.IntegerField()
	#total_theory_duration_hour = models.DecimalField(max_digits=2,decimal_places=1)
	#total_practical_duration_hour = models.DecimalField(max_digits=2,decimal_places=1)
	#total_theory_marks = models.IntegerField()
	#total_practical_marks = models.IntegerField()
	total_final_marks = models.IntegerField()


	def __str__(self):
		return '%s ' % (str(self.syllabus_name))







class Subject(models.Model):
	Subject_code = models.CharField(max_length=25)
	subject_name = models.CharField(max_length=100)
	subject_type = models.CharField(max_length=50, help_text='Compulsory')   #compulsory or elective
	# hours_type = 
	lecture_hours = models.DecimalField(max_digits=2 ,decimal_places=1)
	tutorial_hours = models.DecimalField(max_digits=2,decimal_places=1)
	practical_hours = models.DecimalField(max_digits=2,decimal_places=1)

	Total_no_of_hours = models.DecimalField(max_digits=2,decimal_places=1)

	syllabus = models.ManyToManyField(Syllabus)



	exam_type = models.CharField(max_length=10)

	def __str__(self):
		return '%s ' % (self.subject_name)

	# @property
	# def no_of_hours(self):
	# 	return self.lecture_hours + self.tutorial_hours + self.practical_hours

	# no_of_hours = models.DecimalField(max_digits=2,decimal_places=1,default=calculate_no_of_hr)









class Marks(models.Model):
	
	class Meta:
		verbose_name_plural = 'Marks'

	subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)



	practical_assessment_total = models.IntegerField()
	# practical_assessment_pass = models.IntegerField()
	practical_final_total = models.IntegerField()
	# practical_final_pass = models.IntegerField()
	theory_assessment_total = models.IntegerField()
	# theory_assessment_pass = models.IntegerField()
	theory_final_total = models.IntegerField()
	# theory_final_pass = models.IntegerField()
	marks_final_total = models.IntegerField()

	theory_duration_hours = models.DecimalField(max_digits=2,decimal_places=1)
	practical_duration_hours = models.DecimalField(max_digits=2,decimal_places=1)

	def __str__(self):
		return '%s ' % (self.subject_id.subject_name)





from django.db import models
from . import choices

#Department
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
	dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)
	# syllabus_id = 
	level = models.ForeignKey('Level', on_delete =models.CASCADE)

	def __str__(self):
		return '%s' % (self.program_name)


# class Marks(models.Model):
	
# 	class Meta:
# 		verbose_name_plural = 'Marks'

# 	subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)



# 	practical_assessment_total = models.IntegerField()
# 	# practical_assessment_pass = models.IntegerField()
# 	practical_final_total = models.IntegerField()
# 	# practical_final_pass = models.IntegerField()
# 	theory_assessment_total = models.IntegerField()
# 	# theory_assessment_pass = models.IntegerField()
# 	theory_final_total = models.IntegerField()
# 	# theory_final_pass = models.IntegerField()
# 	marks_final_total = models.IntegerField()

# 	theory_duration_hours = models.DecimalField(max_digits=2,decimal_places=1)
# 	practical_duration_hours = models.DecimalField(max_digits=2,decimal_places=1)

# 	def __str__(self):
# 		return '%s ' % (self.subject_id.subject_name)


class Subject(models.Model):
	Subject_code = models.CharField(max_length=25)
	subject_name = models.CharField(max_length=100)
	# subject_type = models.IntegerField(choices = choices.SUBJECT_TYPE_CHOICES, default = 1)#help_text='Compulsory')   #compulsory or elective
	subject_type = models.CharField(choices = choices.SUBJECT_TYPE_CHOICES,max_length=20, default = 'COMPULSORY')#help_text='Compulsory')   #compulsory or elective
	# hours_type = 
	lecture_hours = models.DecimalField(max_digits=2 ,decimal_places=1,null=True, blank=True)
	tutorial_hours = models.DecimalField(max_digits=2,decimal_places=1,null=True, blank=True)
	practical_hours = models.DecimalField(max_digits=2,decimal_places=1,null=True, blank=True)

	Total_no_of_hours = models.DecimalField(max_digits=2,decimal_places=1)
	# marks_id = models.ForeignKey('Marks',on_delete=models.DO_NOTHING)


	# syllabus = models.ManyToManyField(Syllabus)

	practical_assessment_total = models.IntegerField(null=True, blank=True)
	# practical_assessment_pass = models.IntegerField()
	practical_final_total = models.IntegerField(null=True, blank=True)
	# practical_final_pass = models.IntegerField()
	theory_assessment_total = models.IntegerField(null=True, blank=True)
	# theory_assessment_pass = models.IntegerField()
	theory_final_total = models.IntegerField(null=True, blank=True)
	# theory_final_pass = models.IntegerField()
	marks_final_total = models.IntegerField(null=True, blank=True)

	theory_duration_hours = models.DecimalField(max_digits=2,decimal_places=1, null=True, blank=True)
	practical_duration_hours = models.DecimalField(max_digits=2,decimal_places=1, null=True, blank=True)

	# exam_type = models.IntegerField(choices=choices.EXAM_TYPE_CHOICES, default=1)
	exam_type = models.CharField(choices=choices.EXAM_TYPE_CHOICES,max_length=20, default='Theory')


	def __str__(self):
		return '%s ' % (self.subject_name)

	# @property
	# def no_of_hours(self):
	# 	return self.lecture_hours + self.tutorial_hours + self.practical_hours

	# no_of_hours = models.DecimalField(max_digits=2,decimal_places=1,default=calculate_no_of_hr)



class Syllabus(models.Model):
	
	class Meta:
		verbose_name_plural = 'Syllabus'


	syllabus_id = models.AutoField(primary_key=True)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	syllabus_name = models.CharField(max_length=50,  help_text='BCT_I_I_Part')
	# syllabus_code = models.CharField(max_length=40)
	year = models.IntegerField()
	part = models.IntegerField()
	Subject = models.ManyToManyField(Subject)
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







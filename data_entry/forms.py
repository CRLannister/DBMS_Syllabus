from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Department,Program,Syllabus,Subject,Level

SELECT_DEGREE = (
	('level', 'Level'),
    ('bachelors', 'Bachelors'),
    ('masters', 'Masters'),
)

SELECT_FACULTY = (
	('programs', 'Programs'),
	('BCT', 'BCT'),
	('BEX', 'BEX'),
	('BME', 'BME'),
	('BCE', 'BCE'),
	('BEL', 'BEL'),
	('MSCSKE', 'MSCSKE'),
	('MSICE', 'MSICE'),
)

SELECT_SEMESTER = (
	('semester' , 'Semester'),
	('Semester 1' , 'Semester 1'),
	('Semester 2' , 'Semester 2'),
	('Semester 3' , 'Semester 3'),
	('Semester 4' , 'Semester 4'),
	('Semester 5' , 'Semester 5'),
	('Semester 6' , 'Semester 6'),
	('Semester 7' , 'Semester 7'),
	('Semester 8' , 'Semester 8'),

)

le = Level.objects.all()
le_list = ['Level']
for x in le:
	le_list.append(x.level_name)

le_tuple = tuple(le_list)

pro = Program.objects.all()
pro_list = ['Program']
for x in pro:
	pro_list.append(x.program_name)

pro_tuple = tuple(pro_list)

se = Syllabus.objects.all()
part_set = set()
year_set = set()

for obj in se:
	part_set.add(obj.part)
	year_set.add(obj.year)

part_list = list(part_set)
year_list = list(year_set)
part_list.insert(0,'Part')
year_list.insert(0,'Year')

part_tuple = tuple(part_list)
year_tuple = tuple(year_list)

class process_btn_form(forms.Form):
    degree_choices = le_tuple
    faculty_choices =pro_tuple
    part_choices = part_tuple
    year_choices = year_tuple
    semester_choices = SELECT_SEMESTER



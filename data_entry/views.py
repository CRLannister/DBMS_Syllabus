# from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.views.generic import FormView  
from django.http import HttpResponse
from .forms import process_btn_form
from .models import Syllabus
from . import models
from django.db.models import Q # new
# Create your views here.


select_dict = {'select_degree' : process_btn_form.degree_choices,
				'select_faculty': process_btn_form.faculty_choices,
				'select_year': process_btn_form.year_choices,
				'select_part': process_btn_form.part_choices
	}


def syllabus_dict_list(syllabus_list):
	syllabus_dict = {}
	print("error",syllabus_list)
	for final_syllabus in syllabus_list:
		subject_dict = {'level' : final_syllabus.program.level.level_name}
		subject_dict['program_full_name'] = final_syllabus.program.program_name
		subject_dict['year'] = final_syllabus.year
		subject_dict['part'] = final_syllabus.part
		for subject_var in final_syllabus.Subject.all():
			subject_key = subject_var.Subject_code;
			itr_dict = {}
			itr_dict['Subject_code'] = subject_var.Subject_code
			subject_type = subject_var.subject_type
			subject_name = subject_var.subject_name
			if subject_type == 'Elective':
				subject_name += ' (Elective)'

			itr_dict['subject_name'] = subject_name
			itr_dict['exam_type'] = subject_var.exam_type
			itr_dict['theory_assessment_total'] = subject_var.theory_assessment_total
			itr_dict['theory_final_total'] = subject_var.theory_final_total
			itr_dict['practical_assessment_total'] = subject_var.practical_assessment_total
			itr_dict['practical_final_total'] = subject_var.practical_final_total
			subject_dict[subject_key] = itr_dict

		syllabus_dict[final_syllabus.syllabus_name] = subject_dict
		print(subject_dict)

	return syllabus_dict #{{level:bachelors,syllabus_name:{subjects}}}


def dropdown_search(request):
	level = request.POST.get('Level',default='Bachelors')
	program = request.POST.get('Program',default=None)
	year = request.POST.get('Year',default=1)
	part = request.POST.get('Part',default=1)

	query_program_id = models.Program.objects.all().filter(program_short_name=program)[0].program_id
	if query_program_id != None:
		query_syllabus_set = models.Syllabus.objects.all().filter(program_id = query_program_id)
		final_syllabus = query_syllabus_set
		if type(year) == int:
			final_syllabus = query_syllabus_set.filter(year = year)
		if type(part) == int:
			final_syllabus = query_syllabus_set.filter(part = part)
		
	# final_syllabus = query_syllabus_set.filter(year = year, part= part)
	# final_syllabus = models.Syllabus.objects.all().filter(syllabus_name = final_syllabus)
	print("iterable",final_syllabus)
	syllabus_dict_list1 = syllabus_dict_list(final_syllabus)
	return syllabus_dict_list1
	

def SearchFunc(request, searchQuery):  #bhandari function
    res = [] 
    subs = models.Subject.objects.filter(subject_name__icontains = searchQuery)
    if subs != None:
        subs = list(subs)
        subnames = [x.subject_name for x in subs]
        syllabuses=list(Syllabus.objects.filter())

        for sub in subs:
        	sub_syllabuses = (sub, [])
        	for syl in syllabuses:
        		if sub in syl.Subject.all():
        			sub_syllabuses[1].append(syl)
        	res.append(sub_syllabuses)
    return res  # returns list of tuple of two elements....first element of tuble being subject and other being a list of syllabuses

def home(request):
	print("home_entry ",request)
	if request.method == "GET":
		print("get ",request)
		searchQuery = request.GET.get('q')
		if searchQuery != None:
			search_list = SearchFunc(request, searchQuery)
			print(search_list)

		# return render(request,'data_entry/home.html',{'form': select_dict,'query_list_syllabus': syllabus_dict_list})

		

	if request.method == "POST":
		print("post ",request)
		print(request.POST)
		syllabus_dict_list = dropdown_search(request)
		return render(request,'data_entry/home.html',{'form': select_dict,'query_list_syllabus': syllabus_dict_list})

	
	return render(request,'data_entry/home.html',{'form': select_dict, 'query_list_syllabus':{'level' : 'start' }})

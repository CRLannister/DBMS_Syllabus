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

def get_queryset(request): # new
	query = request.GET.get('q')
	if query != None:
		object_list = models.Subject.objects.filter(Q(subject_name__icontains=query))	#| Q(state__icontains=query)subject_name=query)
		return object_list

def home(request):

	if request.method == "GET":
		search_list = get_queryset(request)
		print(search_list)
		if search_list != None:
			print(search_list)
			# print(request.GET)
			# syllabus_list = models.Syllabus.objects.all().filter(program_id = query_program_id)

	if request.method == "POST":
		print(request.POST)
		# form = process_btn_form(request.POST or None)
		level = request.POST.get('Level',default='Bachelors')
		program = request.POST.get('Program',default=None)
		year = request.POST.get('Year',default=1)
		part = request.POST.get('Part',default=1)

		query_program_id = models.Program.objects.all().filter(program_short_name=program)[0].program_id
		query_syllabus_set = models.Syllabus.objects.all().filter(program_id = query_program_id)
		final_syllabus = query_syllabus_set.filter(year = year, part= part)[0]
		syllabus_dict = {}
		
		# subject_list = [level]
		subject_dict = {'level' : level}
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


		return render(request,'data_entry/home.html',{'form': select_dict,'query_list': subject_dict})

	
	return render(request,'data_entry/home.html',{'form': select_dict, 'query_list':{'level' : 'Masters' }})

from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.views.generic import FormView  
# from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import process_btn_form
from .models import Syllabus
from . import models
# Create your views here.


select_dict = {'select_degree' : process_btn_form.degree_choices,
					'select_faculty': process_btn_form.faculty_choices,
					'select_year': process_btn_form.year_choices,
					'select_part': process_btn_form.part_choices
	}

# def home(request):
def home(request):

	if request.method == "POST":
		level = request.POST.get('Level',default='Bachelors')
		program = request.POST.get('Program',default=None)
		year = request.POST.get('Year',default=1)
		part = request.POST.get('Part',default=1)

		# syllabus = Syllabus.objects.all.filter()
		query_program_id = models.Program.objects.all().filter(program_name=program)[0].program_id
		query_syllabus_set = models.Syllabus.objects.all().filter(program_id = query_program_id)
		final_syllabus = query_syllabus_set.filter(year = year, part= part)[0]
		# for syllabuses in final_syllabus:
		syllabus_dict = {}
		# subject_code_list = []
		# subject_name_list = []
		# subject_exam_type_list = []
		# subject_theory_assessment_total_list = []
		# subject_theory_final_total_list = []
		# subject_practical_assessment_total_list = []
		# subject_practical_final_total_list = []
		subject_list = [level]
		for subject_var in final_syllabus.Subject.all():
			itr_list = []
			# subject_code_list.append(subject_var.Subject_code)
			# subject_name_list.append(subject_var.subject_name)
			# subject_exam_type_list.append(subject_var.exam_type)
			# subject_theory_assessment_total_list.append(subject_var.theory_assessment_total)
			# subject_theory_final_total_list.append(subject_var.theory_final_total)
			# subject_practical_assessment_total_list.append(subject_var.practical_assessment_total)
			# subject_practical_final_total_list.append(subject_var.practical_final_total)
			itr_list.append(subject_var.Subject_code)
			itr_list.append(subject_var.subject_name)
			itr_list.append(subject_var.exam_type)
			itr_list.append(subject_var.theory_assessment_total)
			itr_list.append(subject_var.theory_final_total)
			itr_list.append(subject_var.practical_assessment_total)
			itr_list.append(subject_var.practical_final_total)
			subject_list.append(itr_list)

			# print(subjects)
		# subject_list = [level,subject_code_list,subject_name_list,subject_exam_type_list,subject_theory_assessment_total_list,subject_theory_final_total_list,subject_practical_assessment_total_list,subject_practical_final_total_list]
		return render(request,'data_entry/home.html',{'form': select_dict,'query_list': subject_list})

		# print(form)

	# 	if "process_btn" in request.POST:
	# 		print(request.POST.get('process_btn'))
	# 	else:
	# 		print("fuck no")
	# form = process_btn_form(request.POST or None)
	# print(form)
	
	# answer = form.cleaned_data.get('filter_by')
	# print(answer)
	# model = Syllabus
	# fields = ('program', 'year', 'part')
	# template_name = 'data_entry/index.html'
	# form = process_btn_form(request.POST or None)
	# answer = ''
	
	# return HttpResponse(reverse_lazy('syllabus_display'))
	# form = process_btn_form
	# print(form)
	return render(request,'data_entry/home.html',{'form': select_dict, 'query_list':['Bachelors']})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


from .models import Department, Level, Program, Subject, Syllabus
from serializers import ProgramSerializer#, SyllabusSerializer

# SearchFunc()

def SearchFunc(searchQuery):
    # searchQuery = 'math'    
    subs = Subject.objects.filter(subject_name__icontains = searchQuery)
    subs = list(subs)
    subnames = [x.subject_name for x in subs]
    syllabuses=list(Syllabus.objects.filter())


    res = []

    for sub in subs:
        sub_syllabuses = (sub, [])
        for syl in syllabuses:
            if sub in syl.Subject.all():
                sub_syllabuses[1].append(syl)
    
        res.append(sub_syllabuses)

    return res

    
    

class ProgramList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

# class SubjectList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         program_short_name = self.kwargs['program'].upper()
#         id = Program.objects.get(program_short_name = program_short_name).program_id
#         return [Syllabus.objects.get(year = self.kwargs['year'] ,part = self.kwargs['part'], program_id=id)]

#     serializer_class = SyllabusSerializer

def SubjectList(request, program, year, part):
    program_short_name = program.upper()
    id = Program.objects.get(program_short_name = program_short_name).program_id
    syllabus = Syllabus.objects.get(year = year ,part = part, program_id=id)
    res = {
        'year': syllabus.year,
        'part': syllabus.part,
        'total final marks': syllabus.total_final_marks,
        'syllabus_id': syllabus.syllabus_id,
        'syllabus_name': syllabus.syllabus_name,
        'subjects': [x.subject_name for x in list(syllabus.Subject.all())]
    }
    return JsonResponse(res)

# Functions for dropdown 

def get_syllabus_program_year_part(program,year,part):
    program_short_name = program.upper()
    id = Program.objects.get(program_short_name = program_short_name).program_id
    syllabus_1 = Syllabus.objects.get(year = year ,part = part, program_id=id)
   
    return syllabus_1



def get_syllabus_program_year(program,year):
    program_short_name = program.upper()
    id = Program.objects.get(program_short_name = program_short_name).program_id
    syllabus_1 = Syllabus.objects.get(year = year ,part = 1, program_id=id)
    syllabus_2 = Syllabus.objects.get(year = year ,part = 2, program_id=id)
   
    return [syllabus_1, syllabus_2]


def get_syllabus_year(year):
    programs = list(Program.objects.all())
    res = []
    for prog in programs:
        id = prog.program_id
        syllabus_1 = Syllabus.objects.get(year = year ,part = 1, program_id=id)
        syllabus_2 = Syllabus.objects.get(year = year ,part = 2, program_id=id)
        res.append([syllabus_1, syllabus_2])
    
    return res
    
    
#     program_short_name = 'BCT'
#     id = Program.objects.get(program_short_name = program_short_name).program_id
#     syllabus_1 = Syllabus.objects.get(year = year ,part = 1, program_id=id)
#     syllabus_2 = Syllabus.objects.get(year = year ,part = 2, program_id=id)
#     bct_year_syllabus = [syllabus_1, syllabus_2]
#     program_short_name = 'BEX'
#     id = Program.objects.get(program_short_name = program_short_name).program_id
#     syllabus_1 = Syllabus.objects.get(year = year ,part = 1, program_id=id)
#     syllabus_2 = Syllabus.objects.get(year = year ,part = 2, program_id=id)
#     bex_year_syllabus = [syllabus_1, syllabus_2]
    
#     return [bct_year_syllabus, bex_year_syllabus]

def get_syllabus_program(program):
    #uncomment these lines when data of all 4 years are available
    # and comment the lines after -----------

    # res = []                          
    # for i in range(4):
    #     res.append(get_syllabus_program_year(program, i+1))
    # return res


    #--------------
    program_short_name = program.upper()
    id = Program.objects.get(program_short_name = program_short_name).program_id
    syllabus_program = Syllabus.objects.get(program_id = id)

    return [syllabus_program]


def get_syllabus_bachelors():
    res = []
    res.append(get_syllabus_program('BCT'))
    res.append(get_syllabus_program('BEX'))

    return res

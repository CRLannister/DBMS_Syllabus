from django.urls import path
from . import views
from .apiviews import ProgramList, SubjectList

urlpatterns = [
        path('',views.home, name='syllabus_display'),
        path('api/bachelors/programs/', ProgramList.as_view(), name = 'program_list'),
        path('api/bachelors/programs/<str:program>/<int:year>/<int:part>/', SubjectList, name = 'subject_list' ),
        # path('api/bachelors/<str:subject>', )
]

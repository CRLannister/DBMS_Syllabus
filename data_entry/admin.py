from django.contrib import admin

# Register your models here.

from .models import Department, Syllabus, Marks, Subject, Program

admin.site.register(Department)
admin.site.register(Syllabus)
admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(Program)

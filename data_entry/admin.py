from django.contrib import admin

# Register your models here.

from .models import Department, Syllabus, Subject, Program, Level

admin.site.register(Department)
admin.site.register(Syllabus)
# admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(Program)
admin.site.register(Level)


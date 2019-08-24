from rest_framework import serializers

from .models import Department, Level, Program, Subject, Syllabus

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(many = True, required = False)

    class Meta:
        model = Syllabus
        fields = '__all__'
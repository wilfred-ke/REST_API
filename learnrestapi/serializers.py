from rest_framework import serializers
from .models import Drinks, Members,Courses

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'description']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'fname', 'lname']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'school']

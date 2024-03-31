from django.http import JsonResponse
from .models import Drinks, Members, Courses
from .serializers import DrinkSerializer, MemberSerializer, CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["GET", "POST"])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer2 = CourseSerializer(courses, many=True)
        return Response(serializer2.data)

    if request.method == 'POST':
        serializer2 = CourseSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Members.objects.all()
        serializer1 = MemberSerializer(members, many=True)
        return Response(serializer1.data)

    if request.method == 'POST':
        serializer1 = MemberSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, id):
    try:
        member = Members.objects.get(pk=id)
    except Members.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer1 = MemberSerializer(member)
        return Response(serializer1.data)
    elif request.method == 'PUT':
        serializer1 = MemberSerializer(member, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def course_details(request, id):
    try:
        course = Courses.objects.get(pk=id)
    except Courses.DoesNotExist:
        return Response(satus=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer2 = CourseSerializer(course)
        return Response(serializer2.data)
    elif request.method == 'PUT':
        serializer2 = CourseSerializer(course, data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

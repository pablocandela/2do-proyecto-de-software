from django.shortcuts import render
from aplicacion.models import User,Course,Take
from aplicacion.serializers import UserSerializers,CourseSerializers,TakeSerializers
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class TakeList(generics.ListCreateAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializers

class TakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializers
# Create your views here.

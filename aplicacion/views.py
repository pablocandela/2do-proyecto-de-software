from aplicacion.models import User, Course, Take
from aplicacion.serializers import UserSerializer, CourseSerializer, TakeSerializer
from rest_framework import generics
from django.contrib.auth import login, authenticate
from aplicacion.forms import SignUpForm
from aplicacion.forms import CrearClaseForm
from django.shortcuts import render, redirect


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TakeList(generics.ListCreateAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer


class TakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #este form save, guarda en la base, solo es eso
            form.save()
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def crearClase(request):
    form = CrearClaseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_teacher = form.save(commit = False)
            usuario = User.objects.get(pk=1)
            new_teacher.teacher = usuario
            new_teacher.save()
            
            return redirect('crearClase')
        else:
            form = CrearClaseForm()
    return render(request, 'crearClase.html', {'form': form})


# Create your views here.



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from departement.models import Etudiant
from .form import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext as _
from departement.models import Departement
from departement.serializers import DepartmentSerializer, StudentSerializer


class DepartementView(APIView):
    def get(self, request):
        department = Departement.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class StudentView(APIView):
    def get(self, request):
        student = Etudiant.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def before_login(request):
    context = {}
    return render(request, 'before_login.html', context)


@login_required(login_url='login')
def index(request):
    from django.utils import translation
    user_langage='fi'
    translation.activate(user_langage)
    request.session[translation.LANGUAGE_SESSION_KEY]=user_langage

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    context = {"dic1": "DIC DE L'EPT"}
    return render(request, 'index.html', context)


@login_required(login_url='contact')
def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='list_etudiant')
def list_etudiant(request):
    query_results = Etudiant.objects.filter(dept='GIT')
    return render(request, 'list_etudiant.html', {'query_results': query_results})


@login_required(login_url='list_etudiant_civil')
def list_etudiant_civil(request):
    query = Etudiant.objects.filter(dept='GC')
    return render(request, 'list_etudiant_civil.html', {'query': query})


@login_required(login_url='administration')
def administration(request):
    return render(request, 'administration.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + '' + username)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        form = UserForm()
        return render(request, 'inscription.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'before_login.html')

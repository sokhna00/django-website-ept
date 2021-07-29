from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .forms import EtudiantForm
from .models import Etudiant
from .models import User


def git(request):
    if request.method == "POST":
        return redirect('/dept/deptgit')
    else:
        form = EtudiantForm()
    return render(request, 'git.html', {'form': form})


def civil(request):
    if request.method == "POST":
        return redirect('/dept/deptcivil')
    else:
        form = EtudiantForm()
    return render(request, 'civil.html', {'form': form})


def list_etudiant(request):
    query_results = Etudiant.objects.all()
    return render(request, 'list_etudiant.html', {'query_results': query_results})


def Register(request):
    if request.method == "POST":
        username = request.POST['firstpname']
    fname = request.POST['firstname']
    lname = request.POST['adress']
    email = request.POST['email']
    password = request.POST['password']

    u = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
    u.save()

    return HttpResponse(
        "Registration complete! Please head over to the <a href='/login/'>login page</a> to start using your website.")

    return render(request, "index.html", {})

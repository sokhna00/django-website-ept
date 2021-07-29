from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from departement import views

urlpatterns = [
    path('deptgit/', views.git, name='genie_git'),
    path('admin/', admin.site.urls),
    path('deptgit/list_etudiant/', views.list_etudiant, name='list_etudiant'),
    path('deptcivil/', views.civil, name='genie_civil'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.before_login, name='before_login'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('list_etudiant/', views.list_etudiant, name='list_etudiant'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('list_etudiant_civil/', views.list_etudiant_civil, name='list_etudiant_civil'),
    path('administration/', views.administration, name='administration'),

]

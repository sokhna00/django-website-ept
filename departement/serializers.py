from rest_framework import serializers
from .models import Departement,Etudiant
from django import forms


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

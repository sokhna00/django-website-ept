from django.forms import ModelForm
from .models import Etudiant


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['mail_etudiant', 'password', 'date_de_naissance', 'lieu_de_naissance']

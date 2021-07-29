from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Professeur(models.Model):
    contact_prof = models.CharField(max_length=100)
    date_d_adhesion = models.CharField(max_length=100)
    chef_departement = models.BooleanField(max_length=100)
    # departement=models.ManyToManyField(Departement,related_name='professeur',blank=True)


class Departement(models.Model):
    nom_departement = models.CharField(max_length=100)
    mail_departement = models.EmailField(max_length=100)
    numero_departement = models.CharField(max_length=80, default="")
    description_dept = models.TextField(default="")
    professeur = models.ManyToManyField(Professeur, related_name='departement', blank=True)

    def __str__(self):
        return f"{self.nom_departement}"


class User(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    class Meta:
        abstract = True


class Etudiant(models.Model):
    choix = [
        ('GIT', 'GIT'),
        ('GC', 'GC'),
        ('GEM', 'GEM'),
        ('AERO', 'AERO'),
    ]
    mail_etudiant = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_de_naissance = models.CharField(max_length=100)
    lieu_de_naissance = models.CharField(max_length=100)
    dept = models.CharField(default='GIT', max_length=100, choices=choix)

    def __str__(self):
        return f"{self.mail_etudiant}"


class Classe(models.Model):
    nom_classe = models.CharField(max_length=100)
    description_classe = models.TextField(max_length=100)
    etudiant = models.ManyToManyField(Etudiant, related_name='classe', blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_classe}"


class UE_matiere(models.Model):
    nom_UE = models.CharField(max_length=100)
    code_UE = models.IntegerField
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_UE}"


# coef_UE=
# credit_UE=


class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=100)
    code_matiere = models.CharField(max_length=100)
    coef_matiere = models.IntegerField
    credit_matiere = models.IntegerField
    quota_horaire = models.CharField(max_length=100)
    description_matiere = models.TextField(max_length=100)
    ue_matiere = models.ForeignKey(UE_matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_matiere}"


class Inscription(models.Model):
    annee_scolaire = models.DateField(max_length=100)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

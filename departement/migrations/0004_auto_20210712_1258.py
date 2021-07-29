# Generated by Django 3.2.3 on 2021-07-12 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0003_auto_20210707_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_classe', models.CharField(max_length=100)),
                ('description_classe', models.TextField(max_length=100)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_etudiant', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('date_de_naissance', models.CharField(max_length=100)),
                ('lieu_de_naissance', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_prof', models.CharField(max_length=100)),
                ('date_d_adhesion', models.CharField(max_length=100)),
                ('chef_departement', models.BooleanField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UE_matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_UE', models.CharField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_matiere', models.CharField(max_length=100)),
                ('code_matiere', models.CharField(max_length=100)),
                ('quota_horaire', models.CharField(max_length=100)),
                ('description_matiere', models.TextField(max_length=100)),
                ('ue_matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.ue_matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_scolaire', models.DateField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.classe')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='etudiant',
            field=models.ManyToManyField(blank=True, related_name='classe', to='departement.Etudiant'),
        ),
        migrations.AddField(
            model_name='departement',
            name='professeur',
            field=models.ManyToManyField(blank=True, related_name='departement', to='departement.Professeur'),
        ),
    ]

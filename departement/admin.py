from django.contrib import admin
from departement.models import Departement
from departement.models import Classe
from departement.models import Professeur
from departement.models import UE_matiere
from departement.models import Etudiant
from departement.models import Matiere
from departement.models import Inscription
from django.contrib.auth.models import Group


admin.site.site_header = 'Page Admin EPT'


class DepartementAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('nom_departement', 'mail_departement')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('numero_departement', 'description_dept'),
        }),
    )
    list_display = ('nom_departement', 'mail_departement')


admin.site.register(Departement, DepartementAdmin)
admin.site.register(Classe)
admin.site.register(Professeur)
admin.site.register(UE_matiere)
admin.site.register(Etudiant)
admin.site.register(Matiere)
admin.site.register(Inscription)
admin.site.unregister(Group)

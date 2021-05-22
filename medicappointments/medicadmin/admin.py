from django.contrib import admin
from django.contrib.admin import AdminSite

from medicmodels.models import (
    TypeOfVisit,
    Medic,
    Patient,
    Visit,
    Appointment
)


class MedicAdminSite(AdminSite):
    site_header = 'Medics agenda administration'


class PossibleVisitsByMedicInline(admin.TabularInline):
    model = Medic.medic_specializations.through
    extra = 1


class MedicAdmin(admin.ModelAdmin):
    inlines = [
        PossibleVisitsByMedicInline,
    ]


admin_site = MedicAdminSite(name='medicadmin')

admin_site.register(TypeOfVisit)
admin_site.register(Patient)
admin_site.register(Visit)
admin_site.register(Appointment)

admin_site.register(Medic, MedicAdmin)

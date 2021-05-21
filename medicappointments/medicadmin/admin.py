from django.contrib import admin

from medicmodels.models import (
    TypeOfVisit,
    Medic,
    Patient,
    Visit,
    Appointment
)


admin.site.register(TypeOfVisit)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Appointment)


#class PatientInline(admin.TabularInline):
#    model = Patient
class PossibleVisitsByMedicInline(admin.TabularInline):
    model = Medic.medic_specializations.through


class MedicAdmin(admin.ModelAdmin):
    inlines = [
        PossibleVisitsByMedicInline,
    ]


admin.site.register(Medic, MedicAdmin)

from django.contrib import admin

from medicmodels.models import (
    TypeOfVisit,
    Medic,
    Patient,
    Visit,
    Appointment
)


admin.site.register(TypeOfVisit)
admin.site.register(Medic)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Appointment)


#class PatientInline(admin.TabularInline):
#    model = Patient

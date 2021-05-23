from django.contrib import admin
from django.contrib.admin import AdminSite
from django.forms.models import BaseInlineFormSet

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
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


class MedicAdmin(admin.ModelAdmin):
    inlines = [
        PossibleVisitsByMedicInline,
    ]


class PatientAppointmentsInline(admin.TabularInline):
    model = Appointment
    extra = 1


class VisitsCarriedOutInlineFormSet(BaseInlineFormSet):

    def get_queryset(self):
        qs = super(VisitsCarriedOutInlineFormSet, self).get_queryset()
        return qs.filter(visit__isnull=False)


class PatientVisitsInline(admin.TabularInline):
    """
    This is a normal Patient-Appointment Inline, but appointments are filtered by VISIT!=NULL
    """
    model = Appointment
    formset = VisitsCarriedOutInlineFormSet
    extra = 0
    readonly_fields = ('type', 'medic', 'visit', 'date',)
    fields = ('date', 'visit', 'type', 'medic')
    can_delete = False
    verbose_name = "Visit"
    verbose_name_plural = "Visits"

    def has_add_permission(self, request, obj=None):
        return False


class PatientAdmin(admin.ModelAdmin):
    model = Patient
    inlines = [
        PatientAppointmentsInline,
        PatientVisitsInline,
    ]


admin_site = MedicAdminSite(name='medicadmin')

admin_site.register(TypeOfVisit)
admin_site.register(Patient, PatientAdmin)
admin_site.register(Visit)
admin_site.register(Appointment)

admin_site.register(Medic, MedicAdmin)

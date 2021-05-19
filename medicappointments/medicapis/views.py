from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TypeOfVisitSerializer
from .serializers import MedicSerializer
from .serializers import PatientSerializer
from .serializers import VisitSerializer
from .serializers import AppointmentSerializer
from medicmodels.models import (
    TypeOfVisit,
    Medic,
    Patient,
    Visit,
    Appointment
)


class TypeOfVisitViewSet(viewsets.ModelViewSet):
    queryset = TypeOfVisit.objects.all()
    serializer_class = TypeOfVisitSerializer


class MedicViewSet(viewsets.ModelViewSet):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

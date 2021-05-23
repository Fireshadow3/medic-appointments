from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django_filters import rest_framework as filters
from rest_framework import generics
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


class AppointmentFilterByMedic(filters.FilterSet):
    start_date = filters.IsoDateTimeFilter(field_name="date", lookup_expr='gte')
    end_date = filters.IsoDateTimeFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = Appointment
        fields = ['medic', 'type']


class AppointmentFilterByPatient(filters.FilterSet):
    start_date = filters.IsoDateTimeFilter(field_name="date", lookup_expr='gte')
    end_date = filters.IsoDateTimeFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = Appointment
        fields = ['patient', 'type']


class AppointmentsFilteredListByMedic(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppointmentFilterByMedic


class AppointmentsFilteredListByPatient(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppointmentFilterByPatient

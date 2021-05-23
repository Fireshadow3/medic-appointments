from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from .serializers import TypeOfVisitSerializer
from .serializers import MedicSerializer
from .serializers import PatientSerializer
from .serializers import VisitSerializer
from .serializers import AppointmentSerializer
import datetime
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


@api_view()
def listVisitsByUserByDay(request):

    date = request.query_params.get('date')

    if date is None:
        return Response("Date missing from URL query", status=status.HTTP_400_BAD_REQUEST)

    try:
        dateParsed = datetime.datetime.strptime(date, '%Y-%m-%d')
    except Exception as e:
        return Response("Wrong date format:"+str(e), status=status.HTTP_400_BAD_REQUEST)

    returnData = {}

    appointmentsThatDay = Appointment.objects.filter(date__date=dateParsed, visit__isnull=False)
    if len(appointmentsThatDay) > 0:
        for appointment in appointmentsThatDay:

            visitdata = {
                "date": appointment.date,
                "visit": {
                    "result":appointment.visit.result,
                    "notes":appointment.visit.notes
                }
            }

            if returnData.get(appointment.patient.pk) is not None:
                returnData[appointment.patient.pk].append(visitdata)
            else:
                returnData[appointment.patient.pk] = [visitdata]

    else:
        Response("No visits for the day given", status=status.HTTP_404_NOT_FOUND)

    return Response(returnData)

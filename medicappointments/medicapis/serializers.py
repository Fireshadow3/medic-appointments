from rest_framework import serializers
from medicmodels.models import (
    TypeOfVisit,
    Medic,
    Patient,
    Visit,
    Appointment
)


class TypeOfVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeOfVisit
        fields = '__all__'


class MedicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medic
        fields = '__all__'


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('name', 'surname')


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

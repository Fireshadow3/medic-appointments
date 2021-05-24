from django.db import models
from django.core.exceptions import ValidationError


class TypeOfVisit(models.Model):
    """
    Type of a visit a medic may execute.
    Related to :model:`Medic` for the types of visits the medic can execute.
    Related to :model:`Visit` for the type of the visit.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Medic(models.Model):
    """
    Stores a medic.
    Related to :model:`TypeOfVisit` for the types of visits the medic can execute.
    """
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)
    medic_specializations = models.ManyToManyField(TypeOfVisit)

    def __str__(self):
        return self.name+" "+self.surname


class Patient(models.Model):
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)

    def __str__(self):
        return self.name+" "+self.surname


class Appointment(models.Model):
    type = models.ForeignKey(TypeOfVisit, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    medic = models.ForeignKey(Medic, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    def clean(self):
        """
        Don't allow for an appointment to have a type of visit that a medic can't execute
        """
        medic_specializations = self.medic.medic_specializations.all()
        if (self.type not in medic_specializations):
            raise ValidationError("Medic doesn\'t have the specified visit type "+str(self.type))

    def __str__(self):
        return str(self.type)+","+str(self.date)


class Visit(models.Model):
    result = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.result

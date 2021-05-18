from django.db import models


class TypeOfVisit(models.Model):
    """
    Type of a visit a medic may execute.
    Related to :model:`Medic` for the types of visits the medic can execute.
    Related to :model:`Visit` for the type of the visit.
    """
    name = models.CharField(max_length=100)


class Medic(models.Model):
    """
    Stores a medic.
    Related to :model:`TypeOfVisit` for the types of visits the medic can execute.
    """
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)
    medic_specializations = models.ManyToManyField(TypeOfVisit)


class Patient(models.Model):
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)


class Visit(models.Model):
    result = models.TextField(blank=True)
    notes = models.TextField(blank=True)

class Appointment(models.Model):
    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(TypeOfVisit, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()

from django.db import models


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
        return self.name+self.surname


class Patient(models.Model):
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)

    def __str__(self):
        return self.name+self.surname


class Visit(models.Model):
    result = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.result


class Appointment(models.Model):
    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.ForeignKey(TypeOfVisit, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()

    def __str__(self):
        return self.type+self.date

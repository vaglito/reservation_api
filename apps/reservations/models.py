from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ModelBase(models.Model):
    is_active = models.BooleanField(
        "Estado",
        default=True
    )
    created_at = models.DateTimeField(
        "Creacion",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Actualizado",
        auto_now=True,
    )

    class Meta:
        abstract = True
    

class Table(ModelBase):
    DISPONIBLE = "D"
    OCUPADA = "O"
    EN_RESERVA = "R"
    number = models.IntegerField("Numero de mesa", unique=True)
    STATE_CHOICES = {
        DISPONIBLE: "Disponible",
        OCUPADA: "Ocupada",
        EN_RESERVA: "En Reserva",
    }

    state = models.CharField(
        "Estado",
        max_length=3,
        choices=STATE_CHOICES,
        default=DISPONIBLE
    )
    capacity = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.number}"
    
    class Meta:
        ordering = ['capacity']
        db_table = 'Mesas'


class Reservation(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField("Hora de reserva")
    duration_hours = models.IntegerField("Duracion de Reserva")

    def __str__(self):
        return f"{self.user.email} - Mesa {self.table.number} - {self.reserved_at}"
    
    class Meta:
        db_table = 'Reservas'

from django.db import models

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class PlanSalud(models.Model):
    nombre = models.CharField(max_length=100)
    cobertura = models.TextField()
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE, related_name="planes")

    def __str__(self):
        return f"{self.nombre} - {self.obra_social.nombre}"


class Afiliado(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    id_afiliado = models.CharField(max_length=15, unique=True)
    plan_salud = models.ForeignKey(PlanSalud, on_delete=models.CASCADE, related_name="afiliados")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"

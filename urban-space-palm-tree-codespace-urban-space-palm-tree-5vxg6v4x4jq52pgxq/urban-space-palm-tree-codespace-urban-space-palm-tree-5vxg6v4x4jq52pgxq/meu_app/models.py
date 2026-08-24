from django.db import models


class Equipamento(models.Model):
    nome = models.CharField(max_length=150)
    numero_patrimonio = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=100)
    em_uso = models.BooleanField(default=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

    def __str__(self):
        return f"{self.nome} - Patrimônio {self.numero_patrimonio}"

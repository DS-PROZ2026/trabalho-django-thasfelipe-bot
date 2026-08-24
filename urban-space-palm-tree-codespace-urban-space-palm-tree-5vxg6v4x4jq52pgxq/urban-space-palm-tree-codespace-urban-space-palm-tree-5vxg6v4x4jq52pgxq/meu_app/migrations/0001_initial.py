# Generated for the Sistema de Gestão de Ativos.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipamento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=150)),
                ("numero_patrimonio", models.PositiveIntegerField(unique=True)),
                ("tipo", models.CharField(max_length=100)),
                ("em_uso", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Equipamento",
                "verbose_name_plural": "Equipamentos",
                "ordering": ["nome"],
            },
        ),
    ]

from django.db import models


class Familiares(models.Model):
    nombre_completo = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
    edad = models.IntegerField(default=0)
    fecha_nacimiento = models.DateField(auto_now=True)


# Una migracion es un nuevo cambio
# Mira si hemos creado nuevas tablas y prepara el archivo
# para agregar esas tablas

# python manage.py makemigrations

# Crea las tablas en el archivo
# python manage.py migrate


# Para agregar informacion uno de los metodos es
# python manage.py shell

# Cuando estamos en modo python
# 1. Importar tabla
    # from familia.models import Familiares

# Crear variable con una nueva fila para la tabla

# nuevo_familiar = Familiares(
#     nombre_completo="María Paz",
#     edad=30,
#     profesion="Programadora",
#     email = "maria@gmali.com",
#     descripcion = "sqwjhqwkjehqwkjehqwkeqkeqñlwejñlqkeñlqkweoasd",
# )

# nuevo_familiar.save()





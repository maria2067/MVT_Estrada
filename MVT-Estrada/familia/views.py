from django.shortcuts import render
from .models import Familiares
import random

# Create your views here.
def pagina_principal_familia(request):

    mis_datos = {
        "familiares": Familiares.objects.all().values()
    }

    return render(request, 'familia/familia.html', mis_datos)
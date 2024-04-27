from django.shortcuts import render
from .models import AutorDb, FraseDb
#Se importa el modulo, como se menciono previamente
# from django.http import HttpResponse #Ya no es necesario, ahora se renderiza un HTML

#Luego se crea la funcion nombrandola (no obligatorio) al final con 'View'
def HomeView(request):
  datosAutor = AutorDb.objects.all().order_by("-id")
  datosFrases = FraseDb.objects.all().order_by("-id")
  return render(request, "index.html", {"datosAutor": datosAutor, "datosFrases": datosFrases})
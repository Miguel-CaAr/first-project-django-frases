from django.contrib import admin
from .models import AutorDb, FraseDb #Se importan los modelos

class FraseInLine(admin.TabularInline): #Clase para poder manipular Frases desde el formulario Autores
  model = FraseDb
  extra = 1

# Registro de los modelos instanciando de ModelAdmin
class AutorAdmin(admin.ModelAdmin):
  #Campos que se mostraran y ppodran modificar en el formulario
  fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'profesion', "nacionalidad"]
  #Campos que se mostraran en el listado de los registros
  list_display = ['nombre', 'fecha_nacimiento', 'nacionalidad']

  inlines = [FraseInLine] # Agregar las Frases que sera accesible desde el formulario de Autor

  def inicialEnMayuscula(self, request, queryset):
    nombreinicialesMayusculas = "" #Variable que almacenara el nombre actualizado
    for obj in queryset: #itera todos los campos seleccinados en la tabla
      nombres = obj.nombre.split() #Se divide cada palabra(nombre) separada por un espacio en blanco (por defecto)
      for nombre in nombres: #Se iteran esas nombres divididas
        nombreinicialesMayusculas += (nombre.capitalize() + " ") #Pone mayuscula a la inical del nombre y lo adiciona junto a un espacio
      obj.nombre = nombreinicialesMayusculas #Se asigna el nombre actualizado al nombre del campo
      obj.save() # Se guarda en la BD
      nombreinicialesMayusculas = '' # Se limpia el nombre actualizado
    
    self.message_user(request, "Actualizacion exitosa") #Mensaje una vez terminada la funcion
    
  inicialEnMayuscula.short_description = 'Iniciales en mayuscula' #Descripcion para el select del /admin
  
  actions = ["inicialEnMayuscula"] #Se agrega la accion
  
#Aqui se registra en el admin el modelo AutorDb junto a la configuracion personalizada AutorAdmin
admin.site.register(AutorDb, AutorAdmin)

#Aqui se usara un decorador para registrar en el admin el modelo FraseAdmin
@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
  fields = ['cita', 'autor_fk']
  list_display = ['cita'] 
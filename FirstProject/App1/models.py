from django.db import models

# Create your models here.
class AutorDb(models.Model):
  nombre = models.CharField(max_length=75, verbose_name="Nombre del autor")
  fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=False, blank=False)
  fecha_fallecimiento = models.DateField(verbose_name="Fecha de fallecimiento", null=True, blank=True)
  profesion = models.CharField(verbose_name="Profesión del autor", max_length=50)
  nacionalidad = models.CharField(verbose_name="Nacionalidad del autor", max_length=50)
  
  class Meta:
    db_table = "Autores"
    verbose_name = "Autor"
    verbose_name_plural = "Autores"
    
  def __str__(self) -> str:
      return self.nombre
  
  
class FraseDb(models.Model):
  cita = models.TextField(verbose_name="Cita", max_length=500)
  autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
  
  class Meta:
    db_table = "Frases"
    verbose_name = "Frase"
    verbose_name_plural = "Frases"
  
  def __str__(self) -> str:
      return self.cita
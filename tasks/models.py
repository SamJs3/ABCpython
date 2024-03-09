from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre', 'apellido', 'correoElectronico', 'fechaNacimiento']
    
    
    
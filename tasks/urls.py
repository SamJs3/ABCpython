#from django.urls import path 
#from .views import list_tasks, create_task, delete_task

#urlpatterns = [
#    path('', list_tasks),
#    path('new/', create_task), #nueva ruta para guardar datos 
#    path('delete_task/<int:task_id>/', delete_task, name='delete_task'), #aca le damos el valor del id que vamos a borrar
#]

from django.urls import path 
from .views import list_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task), # Ruta para crear una nueva tarea
    path('update_task/<int:task_id>/', update_task, name='update_task'), # Ruta para actualizar una tarea
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'), # Ruta para eliminar una tarea
]
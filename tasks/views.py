from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  #se importa la clase que esta en models 
from .models import TaskForm


# Create your views here.

#esto nos sirve para poder llamar la funcion de list_tasks.html 
#esto se ejecuta cuando se visita la url 
def list_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_tasks.html',{"tasks": tasks})


#nos muestra en la consola los datos que estamos recibiendo en el formulario
def create_task(request):
    task = Task(nombre=request.POST['nombre'], apellido=request.POST['apellido'], correoElectronico=request.POST['correoElectronico'], fechaNacimiento=request.POST['fechaNacimiento'])
    task.save()
    return redirect('/tasks') #envia los datos a la ruta especificada /tasks

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')

def update_task(request, task_id):
    # Obtener la tarea que se va a actualizar
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        # Si el formulario se ha enviado, procesarlo
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Guardar los cambios en la tarea
            form.save()
            # Redirigir al usuario a la página de listado de tareas
            #return render(request, 'list_tasks.html', {'form': form, 'task_id': task_id})
            #return redirect('list_tasks.html')
            return redirect('/tasks/')
        
    else:
        # Si es una solicitud GET, mostrar el formulario de actualización con los datos actuales de la tarea
        form = TaskForm(instance=task)
    
    # Renderizar el formulario de actualización
    return render(request, 'list_tasks.html', {'form': form, 'task_id': task_id})
    
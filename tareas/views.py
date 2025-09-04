from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CrearFom
from .forms import actividad
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def inscripcion(request):

    if request.method == 'GET':
        return render(request, 'inscripcion.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
                #return HttpResponse('Usuario Creado Satisfactoriamente')
            except IntegrityError:
                return render(request, 'inscripcion.html', {
                    'form': UserCreationForm,
                    "error": "Usuario ya existe"
                })
        return render(request, 'inscripcion.html', {
            'form': UserCreationForm,
            "error": "Contraseñas no coinciden"
        })
@login_required
def tareas(request):
    actividades = actividad.objects.filter(user=request.user, f_completada__isnull=True)
    return render(request, 'tareas.html', {'tareas': actividades, 'titulo': 'Tareas Pendientes'})



@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm, 
            'error': 'Usuario o Password son incorrectos'
            })    
        else:
            login(request, user)
            return redirect('tareas')
@login_required
def crear_tareas(request):
    if request.method == 'GET': 
        return render(request, "crear_tareas.html", {
        'form': CrearFom
    }) 
    else:
       try:
        form = CrearFom(request.POST)
        nueva_tarea = form.save(commit=False)
        nueva_tarea.user = request.user
        nueva_tarea.save()
        return redirect('tareas')
       except ValueError:
           return render(request, 'crear_tareas.html', {
               'form': CrearFom,
               'error': 'Por favor introduce datos validos'
           })
@login_required
def detalle_tarea(request, task_id):
    if request.method == 'GET':
        tarea = get_object_or_404(actividad, pk=task_id, user=request.user)
        form = CrearFom(instance=tarea)
        return render(request, 'detalles_tareas.html', {'actividad': tarea, 'form': form})
    else:
        try:
            tarea = get_object_or_404(actividad, pk=task_id, user=request.user)
            form = CrearFom(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detalles_tareas.html', {'actividad': tarea, 'form': form, 'error': "Error al actualizar las tareas "})
@login_required        
def completar(request, task_id):
    tarea= get_object_or_404(actividad, pk=task_id, user=request.user)
    if request.method == 'POST':
        tarea.f_completada = timezone.now()
        tarea.save()
        return redirect('tareas')
@login_required    
def eliminar(request, task_id):
    tarea= get_object_or_404(actividad, pk=task_id, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')
@login_required    
def tareas_completadas(request):
    actividades = actividad.objects.filter(user=request.user, f_completada__isnull=False).order_by('-f_completada')

    return render(request, 'tareas.html', {'tareas': actividades, 'titulo': 'Tareas Completadas'})
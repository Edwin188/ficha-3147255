"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('tareas/', views.tareas, name='tareas'),
    path('logout/', views.signout, name='Cerrar'),
    path('signin/', views.signin, name='Login'),
    path('tareas/crear_tareas/', views.crear_tareas, name='Crear Tareas'),
    path('tareas/<int:task_id>/', views.detalle_tarea, name='detalles_tareas'),
    path('tareas/<int:task_id>/completar', views.completar, name='completar'),
    path('tareas/<int:task_id>/eliminar', views.eliminar, name='eliminar'),
    path('tareas_completadas/', views.tareas_completadas, name='tareas_completadas'),
]

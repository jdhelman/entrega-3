from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-obra-social/', views.agregar_obra_social, name='agregar_obra_social'),
    path('agregar-plan-salud/', views.agregar_plan_salud, name='agregar_plan_salud'),
    path('agregar-afiliado/', views.agregar_afiliado, name='agregar_afiliado'),
]

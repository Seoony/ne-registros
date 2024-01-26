from django.urls import path
from . import views

urlpatterns = [
  path('tipo_deportes/', views.list_tipo_deportes),
  path('tipo_deportes/all/', views.list_all_tipo_deportes),
  path('tipo_deportes/dropdown/', views.list_tipo_deportes_dropdown),
  path('tipo_deportes/<int:pk>/', views.list_tipo_deporte),
  path('tipo_deportes/create/', views.create_tipo_deporte),
  path('tipo_deportes/<int:pk>/update/', views.update_tipo_deporte),
  path('tipo_deportes/<int:pk>/activate/', views.activate_tipo_deporte),
  path('tipo_deportes/<int:pk>/deactivate/', views.deactivate_tipo_deporte),
  path('tipo_deportes/<int:pk>/delete/', views.logic_delete_tipo_deporte),
  path('tipo_deportes/<int:pk>/trueDelete/', views.delete_tipo_deporte),
]
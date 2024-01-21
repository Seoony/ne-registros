from django.urls import path
from . import views

urlpatterns = [
    path('fichas_inscripciones/', views.list_fichas_inscripciones),
    path('fichas_inscripciones/all/', views.list_all_fichas_inscripciones),
    path('fichas_inscripciones/<int:pk>/', views.list_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/update/', views.update_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/activate/', views.activate_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/deactivate/', views.deactivate_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/delete/', views.logic_delete_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/trueDelete/', views.delete_ficha_inscripcion),
    path('fichas_inscripciones/create/', views.create_ficha_inscripcion),
    path('fichas_inscripciones/<int:pk>/tipo_deporte/', views.list_ficha_inscripciones_by_tipo_deporte),
    path('fichas_inscripciones/<int:pk>/socio/', views.list_ficha_inscripciones_by_socio),
]
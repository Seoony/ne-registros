from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('socios/', views.list_socios),
    path('socios/all/', views.list_all_socios),
    path('socios/<int:pk>/', views.list_socio),
    path('socios/create/', views.create_socio),
    path('socios/<int:pk>/update/', views.update_socio),
    path('socios/<int:pk>/activate/', views.activate_socio),
    path('socios/<int:pk>/deactivate/', views.deactivate_socio),
    path('socios/<int:pk>/delete/', views.logic_delete_socio),
    path('socios/<int:pk>/trueDelete/', views.delete_socio),
]
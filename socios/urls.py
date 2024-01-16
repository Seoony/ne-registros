from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('socios/', views.list_socios),
    path('socios/<int:pk>/', views.list_socio),
    path('socios/create/', views.create_socio),
    path('socios/<int:pk>/update/', views.update_socio),
    path('socios/<int:pk>/delete/', views.delete_socio),
]
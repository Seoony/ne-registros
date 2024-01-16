from django.urls import path
from socios import views

urlpatterns = [
    path('socios/', views.socio_list),
    path('socios/<int:pk>/', views.socio_detail),
]
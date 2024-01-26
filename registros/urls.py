from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include("socios.urls")),
  path("", include("tipo_deporte.urls")),
  path("", include("ficha_inscripcion.urls")),
]

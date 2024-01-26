from rest_framework.response import Response
from rest_framework.decorators import api_view
from ficha_inscripcion.serializers import FichaInscripcionSerializer, ShowFichaInscripcionSerializer
from ficha_inscripcion.models import FichaInscripcion

@api_view(['GET'])
def list_all_fichas_inscripciones(request):
  fichas_inscripciones = FichaInscripcion.objects.all()
  serializer = ShowFichaInscripcionSerializer(fichas_inscripciones, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_fichas_inscripciones(request):
  fichas_inscripciones = FichaInscripcion.objects.exclude(estado="*")
  serializer = ShowFichaInscripcionSerializer(fichas_inscripciones, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_ficha_inscripciones_by_socio(request, pk):
  fichas_inscripciones = FichaInscripcion.objects.filter(socio=pk)
  serializer = ShowFichaInscripcionSerializer(fichas_inscripciones, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_ficha_inscripciones_by_tipo_deporte(request, pk):
  fichas_inscripciones = FichaInscripcion.objects.filter(tipo_deporte=pk)
  serializer = ShowFichaInscripcionSerializer(fichas_inscripciones, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  serializer = ShowFichaInscripcionSerializer(ficha_inscripcion, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def create_ficha_inscripcion(request):
  serializer = FichaInscripcionSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def update_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  serializer = FichaInscripcionSerializer(instance=ficha_inscripcion, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def activate_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  ficha_inscripcion.estado = "A"
  ficha_inscripcion.save()
  return Response("Ficha de inscripcion activada")

@api_view(['PUT'])
def deactivate_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  ficha_inscripcion.estado = "I"
  ficha_inscripcion.save()
  return Response("Ficha de inscripcion desactivada")

@api_view(['PUT'])
def logic_delete_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  ficha_inscripcion.estado = "*"
  ficha_inscripcion.save()
  return Response("Ficha de inscripcion eliminada logicamente")

@api_view(['DELETE'])
def delete_ficha_inscripcion(request, pk):
  ficha_inscripcion = FichaInscripcion.objects.get(id=pk)
  ficha_inscripcion.delete()
  return Response("Ficha de inscripcion eliminada")


# Create your views here.

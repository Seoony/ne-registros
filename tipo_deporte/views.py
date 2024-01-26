from rest_framework.decorators import api_view
from rest_framework.response import Response
from tipo_deporte.serializers import TipoDeporteSerializer, SimplifiedTipoDeporteSerializer
from tipo_deporte.models import TipoDeporte
# Create your views here.
@api_view(['GET'])
def list_all_tipo_deportes(request):
  tipo_deportes = TipoDeporte.objects.all()
  serializer = TipoDeporteSerializer(tipo_deportes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_tipo_deportes(request):
  tipo_deportes = TipoDeporte.objects.exclude(estado="*")
  serializer = TipoDeporteSerializer(tipo_deportes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_tipo_deportes_dropdown(request):
  tipo_deportes = TipoDeporte.objects.filter(estado="A")
  serializer = SimplifiedTipoDeporteSerializer(tipo_deportes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  serializer = TipoDeporteSerializer(tipo_deporte, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def create_tipo_deporte(request):
  serializer = TipoDeporteSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def update_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  serializer = TipoDeporteSerializer(instance=tipo_deporte, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def activate_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  tipo_deporte.estado = "A"
  tipo_deporte.save()
  return Response("Tipo de deporte activado")

@api_view(['PUT'])
def deactivate_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  tipo_deporte.estado = "I"
  tipo_deporte.save()
  return Response("Tipo de deporte desactivado")

@api_view(['PUT'])
def logic_delete_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  tipo_deporte.estado = "*"
  tipo_deporte.save()
  return Response("Tipo de deporte eliminado logicamente")

@api_view(['DELETE'])
def delete_tipo_deporte(request, pk):
  tipo_deporte = TipoDeporte.objects.get(id=pk)
  tipo_deporte.delete()
  return Response("Tipo de deporte eliminado")

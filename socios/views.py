from rest_framework.decorators import api_view
from rest_framework.response import Response
from socios.serializers import SocioSerializer, SimplifiedSocioSerializer
from socios.models import Socio

@api_view(['GET'])
def hello_world(request):
  return Response({"message": "Hello, world!"})

@api_view(['GET'])
def list_all_socios(request):
  socios = Socio.objects.all()
  serializer = SocioSerializer(socios, many=True)
  return Response(serializer.data)

@api_view(['GET']) 
def list_socios(request):
  socios = Socio.objects.exclude(estado="*")
  serializer = SocioSerializer(socios, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_socios_dropdown(request):
  socios = Socio.objects.filter(estado="A")
  serializer = SimplifiedSocioSerializer(socios, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def list_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  serializer = SocioSerializer(socio, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def create_socio(request):
  serializer = SocioSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def update_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  serializer = SocioSerializer(instance=socio, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def activate_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "A"
  socio.save()
  return Response("Socio activado")

@api_view(['PUT'])
def deactivate_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "I"
  socio.save()
  return Response("Socio desactivado")

@api_view(['PUT'])
def logic_delete_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "*"
  socio.save()
  return Response("Socio eliminado logicamente")

@api_view(['DELETE'])
def delete_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.delete()
  return Response("Socio eliminado")
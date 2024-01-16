from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from socios.models import Socio
from socios.serializers import SocioSerializer

@csrf_exempt
def socio_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        socios = Socio.objects.all()
        serializer = SocioSerializer(socios, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SocioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def socio_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        socio = Socio.objects.get(pk=pk)
    except Socio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SocioSerializer(socio)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SocioSerializer(socio, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        socio.delete()
        return HttpResponse(status=204)
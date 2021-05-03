from django.shortcuts import render
from .models import Project
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .serializer import ProjectSerializer
import io
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def ProjectAPI(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        print("done")
        serializers = ProjectSerializer(projects, many=True)
        return JsonResponse(serializers.data,safe=False) 

    if request.method == 'POST':
        print(request.body.name)
        serializers = ProjectSerializer(data = request.body)
        
        if serializers.is_valid():
            serializers.save()

        return JsonResponse(serializers.data,safe=False)
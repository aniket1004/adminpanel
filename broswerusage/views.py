from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import BroswerUsageSerializer
from .models import BroswerUsage

# Create your views here.
def BroswerUsageAPI(request):
    if request.method == 'GET':
        broswerusage = BroswerUsage.objects.all()
        serializers = BroswerUsageSerializer(broswerusage, many=True)
        return JsonResponse(serializers.data,safe=False)
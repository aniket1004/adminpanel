from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
from .serializer import MessageSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def MessageAPI(request):
    if request.method == 'GET':
        message = Message.objects.all()
        serializers = MessageSerializer(message,many=True)
        return JsonResponse(serializers.data,safe=False)

@csrf_exempt
def MessageDelete(request,pk):
    if request.method == 'DELETE':
        message = Message.objects.get(id=pk)
        message.delete()
        msg = {'message': 'success'}
        return JsonResponse(msg,safe=False)

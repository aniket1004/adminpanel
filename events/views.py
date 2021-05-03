from django.shortcuts import render
import io
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Event
from .serializers import EventSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def EventAPI(request):
    if request.method == 'GET':
        try:
            event = Event.objects.all()
            serializer = EventSerializer(event,many=True)
            # json_data = JSONRenderer().render(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        except:
            msg = {'msg':'Exception occured'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EventSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            message = {'Message': 'Data inserted'}
            json_data = JSONRenderer().render(message)
            return HttpResponse(json_data,content_type='application/json')
    
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        event = Event.objects.get(id = id)
        serializer = EventSerializer(event,data = python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'message':'Event Updated'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'DELETE':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            event = Event.objects.get(id=id)
            event.delete()
            msg = {'message':'Event deleted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        except:
            msg = {'message':'Exception occured while deleting'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')

def getWithId(request,pk):
    if pk is not None:
        try:
            event = Event.objects.get(id=pk)
            serializer = EventSerializer(event)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        except:
            msg = {'message': 'Exception Occured !!'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')        
    
    msg = {'message': 'Error Occured !!'}
    json_data = JSONRenderer().render(msg)
    return HttpResponse(json_data,content_type='application/json')

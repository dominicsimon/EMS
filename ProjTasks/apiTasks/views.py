from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes= [
     {
            'Endpoint': '/Tasks/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Tasks'
        },
        {
            'Endpoint': '/Tasks/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Task object'
        },
        {
            'Endpoint': '/Tasks/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Task with data sent in post request'
        },
        {
            'Endpoint': '/Tasks/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Task with data sent in post request'
        },
        {
            'Endpoint': '/Tasks/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and existing Task'
        },
    ]
    return Response(routes)
@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)
from django.shortcuts import render

# Create your views here.
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serialiser import JobApplicationSerializer, TypeASerializer, TypeBSerializer
# Task model
from .models import JobApplication

@csrf_exempt
def jobs(request):
    if request.method == 'GET':
        tasks = JobApplication.objects.all()
        serializer = JobApplicationSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        job_application_serializer = JobApplicationSerializer(data=data)

        if job_application_serializer.is_valid():
            job_application = job_application_serializer.save()
            return JsonResponse(job_application_serializer.data, status=201)
        return JsonResponse(job_application_serializer.errors, status=400)

    
@csrf_exempt
def job_detail(request, pk):
    try:
        job = JobApplication.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = JobApplicationSerializer(job, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        job.delete() 
        return HttpResponse(status=204) 
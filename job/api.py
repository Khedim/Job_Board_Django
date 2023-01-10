from .serializers import JobSerializer
from .models import Job
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response({'jobs': serializer.data})

@api_view(['GET'])
def job_detail_api(request, slug):
    job = Job.objects.get(slug=slug)
    serializer = JobSerializer(job)
    return Response({'job': serializer.data})

@api_view(['POST'])
def add_job_api(request):
    pass

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug'

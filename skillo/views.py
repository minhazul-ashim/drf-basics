from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from job.models import Job
from job.serializer import JobSerializer

class JobCategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        jobs = Job.objects.filter(category=id)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
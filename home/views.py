from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class ReceipeAPI(APIView):
    def get(self, request):
        queryset = Receipe.objects.all()
        serializer = ReceipeSerializer(queryset, many=True)
        return Response({
            "status": True,
            "message": "The data is fetched successfully",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = CreateReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "The data is saved successfully",
                "data": serializer.data
            })
        return Response({
            "status": False,
            "message": "The data is not saved",
            "data": serializer.errors
        })
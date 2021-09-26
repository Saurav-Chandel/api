from django.shortcuts import render,HttpResponse
# from django.shortcuts import get_objects_or_404
from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    permission_classes=[permissions.IsAuthenticated]



class herolist(APIView):
    def get(self,request):
        employee=employee.objects.all()
        serializer=employeeSerializer(employees1,many=true)
        return Response(serializer.data)

        
    def post(self):
        pass    
    
  
    

    





    



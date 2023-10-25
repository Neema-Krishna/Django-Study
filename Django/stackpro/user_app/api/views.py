 
from rest_framework.response import Response 
from rest_framework import viewsets
# from rest_framework.views import APIView
from django.contrib.auth.models import User
from user_app.api.serializers import RegistrationSerailizer


class UserView(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=RegistrationSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    

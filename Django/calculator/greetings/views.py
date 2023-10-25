from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

class goodmorningView(APIView):
    def get(self,request,id):
        if id==1:
            return Response(data='good morning all')
        elif id==2:
            return Response(data='good afternoon all')
        else:
            return Response(data='invalid')

class goodafternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data='good afternoon all')
class Time(APIView):
    def get(self,request):
        currenttime=datetime.datetime.now().time()
        return Response(data={"time":currenttime})




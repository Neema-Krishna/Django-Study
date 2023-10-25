from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from api.models import Bookstore
from api.serializers import BookstoreSerializer


# Create your views here.

class Bookstoreview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bookstore.objects.all()
        serializer=BookstoreSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request):
        serializer=BookstoreSerializer(request.data)
        if serializer.is_valid():
            print(serializer.is_valid())
            Bookstore.objects.create(**serializer.is_valid())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.error)
class Bookstoreupdate(APIView):
    def get(self,request,*args,**kwargs):
        print(**kwargs)
        id=kwargs.get('id')
        qs=Bookstore.objects.get(id=id)
        serializer=BookstoreSerializer(qs,many=False)
        return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        print(**kwargs)
        id=kwargs.get('id')
        Bookstore.objects.filter(id=id).delete()
        return Response(data='deleted')


from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Additionview(APIView):
    def post(self,request,id,*args,**kwargs):
        if id==1:
            print('addition')
            print(request.data)
            n1 = int(request.data.get('num1'))
            n2 = int(request.data.get('num2'))
            result = n1 + n2

            return Response(data=result)
        if id==2:
            print('substraction')
            print(request.data)
            n1 = int(request.data.get('num1'))
            n2 = int(request.data.get('num2'))
            result1 = abs(n1-n2)

            return Response(data=result1)
        if id==3:
            print('cube')
            print(request.data)
            n1 = int(request.data.get('num1'))
            n2 = int(request.data.get('num2'))
            result3 = n1**3

            return Response(data=result3)
        if id==4:
            print('prime number')
            print(request.data)
            n1=int(request.data.get('num1'))
            for i in range(2,n1):
                if n1%i==0:
                    return Response(data='not a prime number')
                    break
                else:
                    return Response(data='a prime number')


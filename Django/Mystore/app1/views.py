from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Products,Cart,Reviews
from app1.serializers import ProductSerializers,Productmodelserializers,UserSerializer,CartSerializer,ReviewSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import  authentication,permissions


class Productview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializers(qs,many=True)


        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):

        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class Productdetailview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Products.objects.get(id=id)
        serializer=ProductSerializers(qs)
        return  Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Products.objects.filter(id=id).update(**request.data)
        qs=Products.objects.get(id=id)
        serializer=ProductSerializers(qs,many=False)

        return Response(data=serializer)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Products.objects.filter(id=id).delete()
        return Response(data='deleted')

# class Productviewswtsview(viewsets.ViewSet):
#     def list(self,request,*args,**kwargs):
#         qs=Products.objects.all()
#         serializer=Productmodelserializers(qs,many=True)
#         return Response(data=serializer.data)
#
#     def create(self,request,*args,**kwargs):
#         serializer = Productmodelserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#     def retrieve(self,request,*args,**kwargs):
#         id=kwargs.get('pk')
#         qs=Products.objects.get(id=id)
#         serializer=Productmodelserializers(qs,many=False)
#         return Response(data=serializer.data)
#     def destroy(self,request,*ars,**kwargs):
#         id=kwargs.get('pk')
#         Products.objects.filter(id=id).delete()
#         return Response(data='deleted')
#     # def update(self,request,*args,**kwargs):
#     #     id=kwargs.get('pk')
#     #     Products.objects.filter(id=id).update(**request.data)
#     #     qs=Products.objects.get(id=id)
#     #     serailizer=Productmodelserializers(qs,many=False)
#     #     return Response(data=serailizer.data)
#
#     def update(self,request,*args,**kwargs):
#         id=kwargs.get('pk')
#         obj=Products.objects.get(id=id)
#         serializer=Productmodelserializers(data=request.data,instance=obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     @action(methods=['GET'],detail=False)
#     def categories(self,request,*args,**kwargs):
#
#         qs=Products.objects.values_list('category',flat=True).distinct()
#
#         return Response(data=qs)

class UserView(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class Productmodelviewsetview(viewsets.ModelViewSet):
    serializer_class = Productmodelserializers
    queryset = Products.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def categories(self, request, *args, **kwargs):
        qs = Products.objects.values_list('category', flat=True).distinct()

        return Response(data=qs)

    @action(methods=['POST'],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        item=Products.objects.get(id=id)
        user=request.user
        user.cart_set.create(Product=item)
        return Response(data='item added to cart')

    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get('pk')
        object=Products.objects.get(id=id)
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=object,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=['GET'],detail=True)
    def review(self,request,*args,**kwargs):
        # id=kwargs.get("pk")
        # product=Products.objects.get(id=id)
        product=self.get_object()
        qs=product.reviews_set.all()
        serializer=ReviewSerializer(qs,many=True)
        return Response(data=serializer.data)

class CartModelView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        qs=request.user.cart_set.all()
        serializer= CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    def get_queryset(self,request):
        # qs=Cart.objects.filter(user=self.request.user)
        # return Response(data=qs.data)
        return Cart.objects.filter(user=self.request.user)

class DeleteReview(APIView ):
    def delete(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        Reviews.objects.filter(id=pk).delete()
        return Response(data='DELETED')









from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from rest_framework import serializers
from api.serializers import QuestionModelSerializer,AnswerSerializer
from api.models import QuestionModel,AnswerModel

# Create your views here.

class QuestionView(viewsets.ModelViewSet):
    queryset=QuestionModel.objects.all()
    serializer_class=QuestionModelSerializer
    permission_classes=[permissions.IsAuthenticated]
    # authentication_classes=[authentication.TokenAuthentication]
    
    def perform_create(self,serializer):
        # print(self.request.user)
        serializer.save(user=self.request.user)
    def get_queryset(self):
         
        # serializer=QuestionModelSerializer(queryset,many=True)
        # return QuestionModel.objects.all().exclude(user=self.request.user)
        return QuestionModel.objects.all() 
    
    
    @action(methods=['POST'],detail=True)
    def add_answer(self,request,*args,**kwargs):
        object=self.get_object()
        serializer=AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,question=object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    @action(methods=['GET'],detail=True)
    def answer(self,request,*args,**kwargs):
        pk=self.kwargs['pk']
        question= QuestionModel.objects.get(pk=pk)
        Answer=AnswerModel.objects.filter(question=question)
        serializer=AnswerSerializer(Answer,many=True)
        return Response(data=serializer.data)
    
    
class AnswerView(viewsets.ModelViewSet):
    serializer_class=AnswerSerializer
    queryset=AnswerModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    # authentication_classes=[authentication.TokenAuthentication]
    
    # overriding create method and list method as functionality for this is given already in Questview
    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError('Method not found')
    def list(self,request,*args,**kwargs):
        raise serializers.ValidationError('Method not found')
    def destroy(self,request,*args,**kwargs):
        object=self.get_object()
        if request.user==object.user:
            object.delete()
            return Response('Data deleted')
        else:
            raise serializers.ValidationError('You cannot perform this action')
        
    
    @action(methods=['POST'],detail=True)
    def add_upvote(self,request,*args,**kwargs):
        objects=self.get_object()
        user=request.user
        objects.upvote.add(user)
        return Response(data='upvoted')
        
    
    
 
    
           
        
        
        
    
   
# class AnswerView(generics.CreateAPIView):
#     queryset=AnswerModel.objects.all()
#     serializer_class=QuestionModelSerializer
#     permission_classes=[permissions.IsAuthenticated]
#     authentication_classes=[authentication.TokenAuthentication]
#     def perform_create(self,serializer):
#         id=self.kwargs['pk']
#         question=QuestionModel.objects.get(id=id)
#         serializer.save(user=self.request.user,question=question)

    


from rest_framework import serializers 
from api.models import QuestionModel,AnswerModel


 
class AnswerSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    upvote=serializers.CharField(read_only=True)
    upvote_count=serializers.CharField(read_only=True)
    class Meta:
        model=AnswerModel
        fields='__all__'
        
class QuestionModelSerializer(serializers.ModelSerializer):
    
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    question_answer=AnswerSerializer(read_only=True,many=True)
    class Meta:
        model=QuestionModel
        fields='__all__'
        

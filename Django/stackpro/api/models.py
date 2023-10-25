from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_question')
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    image=models.ImageField(null=True,blank=True,upload_to="images")
    
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def question_answer(self):
        return self.answer.all()
        
         
    
class AnswerModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_answer')
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE,related_name='answer')
    answer=models.CharField(max_length=400)
    upvote=models.ManyToManyField(User,related_name='user_vote')
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.answer
    
    @property
    def upvote_count(self):
        return self.upvote.all().count()
    
    
    
     
    
    
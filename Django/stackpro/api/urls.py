from django.urls import path 
from api.views import QuestionView,AnswerView

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('question',QuestionView,basename='question')
router.register('answer',AnswerView,basename='answer')

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('question/',QuestionView.as_view(),name='question'),
    
]+router.urls
from django.contrib import admin
from django.urls import path
from greetings.views import goodmorningView,goodafternoonView,Time
from operators.views import Additionview




urlpatterns = [
    path('goodmorning/<int:id>',goodmorningView.as_view()),
    path('goodafternoon/',goodafternoonView.as_view()),
    path('time/',Time.as_view()),
    path('add/<int:id>',Additionview.as_view()),
]
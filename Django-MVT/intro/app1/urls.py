from django.urls import path,include
from app1 import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('home1/',views.home1,name='home1'),
    path('home2/',views.home2,name='home2'),
    path('',views.home_page,name='home_page'),
    path('register/',views.Register.as_view(),name='register'),
    path('regview/',views.RegView.as_view(),name='regview'),
    path('regdelete/<int:id>',views.RegDelete.as_view(),name='regdelete'),
    path('login/', views.LoginView.as_view(), name='log_in'),
    path('regform/', views.StudReg.as_view(), name='studreg'),
    path('main/',views.main,name='main'),
    path('child/',views.child,name='child')

]
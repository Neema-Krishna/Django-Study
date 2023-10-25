 
from django.urls import path 
from user_app.api.views import UserView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router=DefaultRouter()

router.register('register',UserView,basename='register')



urlpatterns = [
    # path('register/',UserView ,name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
]+router.urls
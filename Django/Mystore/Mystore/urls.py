"""
URL configuration for Mystore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

# Token 1cade7c3f73720c624937f8b7749fb02374465db


router=DefaultRouter()
# router.register('api/products',views.Productviewswtsview,basename='products')
router.register('api/users',views.UserView,basename='users')
router.register('api/products1',views.Productmodelviewsetview,basename='products1')
router.register('api/carts',views.CartModelView,basename='cart')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',ObtainAuthToken.as_view()),
    path('review/<int:pk>',views.DeleteReview.as_view()),
    path('products',views.Productview.as_view()),
    path('products/<int:id>',views.Productdetailview.as_view())
]+router.urls

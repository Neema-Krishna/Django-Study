from rest_framework import serializers
from app1.models import  Products,Reviews,Cart
from django.contrib.auth.models import User

class ProductSerializers(serializers.Serializer):

    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField()

class Productmodelserializers(serializers.ModelSerializer):
    avg_rating=serializers.FloatField(read_only=True)
    review_count=serializers.SerializerMethodField()

    class Meta:
        model=Products
        fields="__all__"
        # field=['name','price']
    def get_review_count(self,obj):
        pro = Products.objects.get(id=obj.id)
        ratings = Reviews.objects.filter(product_id=obj.id).values_list('rating', flat=True)
        print(ratings)
        if ratings:
            return len(ratings)
        else:
            return 0



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:

       model=Cart
       fields="__all__"
class ReviewSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)


    class Meta:
        model=Reviews
        fields='__all__'


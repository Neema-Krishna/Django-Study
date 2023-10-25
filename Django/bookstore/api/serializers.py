from rest_framework import serializers

class BookstoreSerializer(serializers.Serializer):
    bookname=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()

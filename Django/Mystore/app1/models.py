from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)

    @property
    def avg_rating(self):
        ratings=self.reviews_set.all().values_list('rating',flat=True)
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0

    def __str__(self):

        return self.name

#modelname.objects.create(field1=value,field2=value,...)
#qs=modelname.objects.all()
#qv=modelname.objects.filter(category="phone")
#qs=modelname.objects.all().exclude(category="phone")
#qs=modelname.objects.get(id=1)
#modelname.objects.filter(id=1).update(price=400)
#modelname.objects.filter(price__gt=200)
# __lt=
# __gte=
# __lte=

class Cart(models.Model):
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    comments=models.CharField(max_length=100)

    def __str__(self):
        return self.comments



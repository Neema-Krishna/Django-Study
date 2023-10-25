from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from app1.models import RegistrationModel
from django.urls import reverse
from app1.forms import RegistrationForm,RegistrationModelForm

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello! Welcome</h1>')
def home1(request):
    x='Helllo'
    return HttpResponse(x)
def home2(request):
    x=''
    y=[10,20,30]
    return render(request,'home.html',{'data':x,'data1':y})
def home_page(request):
    return render(request,'home_page.html')
 
def log_in(request):
    return render(request,'login.html')
def main(request):
    return render(request,'main.html')
def child(request):
    return render(request,'child.html')

class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'registration.html')
        
    def post(self,request,*args, **kwargs):
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        education=request.POST.get('education')
        place=request.POST.get('place')
        RegistrationModel.objects.create(name=name,age=age,email=email,phone=phone,
                                   address=address,education=education,place=place )
        return redirect("log_in")
        # Register=RegistrationModel(name=name,age=age,email=email,phone=phone,
        #                            address=address,education=education,place=place )
        # Register.save()
        
        # return render(request,'registration.html')
        
class RegView(View):
    def get(self,request,*args, **kwargs):
        viewdata=RegistrationModel.objects.all()     
        return render(request,'regview.html',{'viewdata':viewdata}) 
class RegDelete(View):
    def get(self,request,*args, **kwargs):
        id=self.kwargs.get('id')
        data=RegistrationModel.objects.get(id=id)
        data.delete()   
        return redirect('regview')
        
    



class LoginView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'login.html')
    
# class StudReg(View):
#     def get(self,request,*args, **kwargs):
#         regform=RegistrationForm()
#         # reform=RegistrationModelForm()
#         return render(request,'formreg.html',{'regform':regform})
    
    
class StudReg(View):
    def get(self,request,*args, **kwargs):
        regform=RegistrationModelForm()
        # reform=RegistrationModelForm()
        return render(request,'formreg.html',{'regform':regform})
    def post(self,request,*args, **kwargs):
        regform=RegistrationModelForm(request.POST)
        if regform.is_valid():
            regform.save()
        return HttpResponse('Saved')
        
        
         

    





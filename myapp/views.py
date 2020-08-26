from django.shortcuts import render
from django.http import HttpResponse
from myapp import forms
# Create your views here.
from myapp import utilities

def home(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid()==False:
            return render(request,"myapp/form.html",{'form':form})

        else:
            data=form.cleaned_data
            pic=data['pic']
            utilities.store_image(pic)
            print(form.cleaned_data)
            
    
    form=forms.SampleForm()
    return render(request,"myapp/form.html",{'form':form})
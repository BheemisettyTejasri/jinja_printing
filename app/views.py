from django.shortcuts import render
def print(request):
    d={'name':'Tejasri','age':20}
    return render(request,'jinja_printing.html',context=d)

# Create your views here.

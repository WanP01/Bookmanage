from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {'name':'双十一，有惊喜'}
    return render(request,'books/index.html',context)
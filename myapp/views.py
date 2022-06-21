from django.shortcuts import render, HttpResponse
import random

topics = [
{'id':1, 'title':'Routing', 'body':'Routing is ...'},
{'id':2, 'title':'View', 'body':'View is ...'},
{'id':3, 'title':'Model', 'body':'Model is ...'}
]

# Create your views here.
def index(request):    
    global topics    
    ol = ''    
    for topic in topics:
        ol += f'<li>{topic["title"]}</li>'        
    
    #return HttpResponse('Welcome!')
    #return HttpResponse('<h1>Random</h1>' + str(random.random()))
    
    return HttpResponse( ol )

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)
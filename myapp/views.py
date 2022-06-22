from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is ...'},
    {'id':2, 'title':'View', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'}
]

def HTMLTemplate(articleTag):
    
    global topics    
    ol = ''    
    for topic in topics:
        ol += f'''<li>
            <a href="/read/{topic["id"]}">{topic["title"]}</a>
        </li>'''
        
    html = f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>        
            <li><a href="/create">Create</a></li>
        </ul>
    </body>
    </html>
    '''    
        
    return html

# Create your views here.
def index(request):        
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    #return HttpResponse('Welcome!')
    #return HttpResponse('<h1>Random</h1>' + str(random.random()))    
    return HttpResponse( HTMLTemplate(article) )

def read(request, id):    
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    
    article = '''
        <form action="/create/">
            <p><input type="text" name="title" id="title" placeholder="title" style="width:500px"></p>
            <p><textarea name="body" placeholder="body" style="width:500px"></textarea></p>
            <p><input type="submit"</p>
        </form>
    
    '''
    
    
    return HttpResponse(HTMLTemplate(article))


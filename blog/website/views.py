from django.shortcuts import render
from .models import Post, Contact


# Create your views here.
def hello_blog(request):
    tecnologias = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados',
                   'Linux', 'Nginx','Uwsgi','Systemclt']
    
    list_posts = Post.objects.filter(deleted=False)
    
    data = {
        'name': 'Curso Django 3',
        'lista': tecnologias,
        'posts': list_posts }

    return render(request, 'index.html', data)

def post_details(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'post_detail.html', {'post':post})

def save_form(request):
    Contact.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        message=request.POST['message']
    )
    return render(request, 'index.html')
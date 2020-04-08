from django.shortcuts import render
from .models import Post


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
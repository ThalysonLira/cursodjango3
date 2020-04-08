from django.shortcuts import render

# Create your views here.
def hello_blog(request):
    tecnologias = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados',
                   'Linux', 'Nginx','Uwsgi','Systemclt']

    data = {'name': 'Curso Django 3', 'lista': tecnologias}
    return render(request, 'index.html', data)
from django.db import models

# Create your models here.
# Categorizacao de conteudo


class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name, self.email)


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    # Define as categorias, tamanho maximo (so sera salvo as abreviacoes no bd) e default
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    # Método criado para retornar a categoria de cada post
    def get_categories_label(self):
        return self.get_categories_display()

    # Exibe o título do post na tela de criar post (admin)
    def __str__(self):
        return self.title

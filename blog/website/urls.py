from django.urls import path, include
from .views import hello_blog, post_details

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_details, name='post_detail'),
]
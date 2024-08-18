# urls.py
from django.urls import path
from .views import homepage  # Certifique-se de que `homepage` é uma função ou classe de view

urlpatterns = [
    path('', homepage, name='homepage'),
]


from django.urls import path

# importe todas as views desse app
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('busca', views.buscar, name='buscar')

]

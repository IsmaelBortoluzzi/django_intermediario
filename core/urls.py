from django.urls import path
from core import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('produto/', views.Produto.as_view(), name='produto'),
    path('contato/', views.Contato.as_view(), name='contato'),
]
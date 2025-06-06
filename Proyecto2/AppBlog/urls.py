
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.detalle_post, name='detalle_post'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
]
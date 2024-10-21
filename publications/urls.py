from django.urls import path
from . import views

urlpatterns = [
    path('', views.publication_list, name='publication-list'),
    path('<int:pk>/', views.publication_detail, name='publication-detail'),
]

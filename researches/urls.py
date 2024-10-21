from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_list, name='research-list'),
    path('<int:pk>/', views.research_detail, name='research-detail'),
]
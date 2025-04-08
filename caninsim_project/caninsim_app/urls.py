from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dogs/', views.DogListView.as_view(), name='dogs'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<int:pk>/', views.pet_details, name='pet.detail'),
]

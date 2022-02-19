from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('adoptions/<int:pk>/', views.PetDetails.as_view(), name='pet.details'),
]

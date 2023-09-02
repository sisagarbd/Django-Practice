from django.urls import path
from first_app import views

app_name = "first_app" 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musitian_details/<pk>/', views.DetailView.as_view(), name='musitian_details'),


]

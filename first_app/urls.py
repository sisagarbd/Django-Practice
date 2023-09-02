from django.urls import path
from first_app import views

app_name = "first_app" 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musitian_details/<pk>/', views.DetailView.as_view(), name='musitian_details'),
    path('add_musitian/', views.AddMusitian.as_view(), name='add_musitian'),
    path('musitian_update/<pk>/', views.UpdateMusitian.as_view(), name='musitian_update'),
    path('delete_musitian/<pk>/', views.DeleteMusitian.as_view(), name='delete_musitian'),

]

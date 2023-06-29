from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/confirm_delete/', views.confirm_delete, name='confirm_delete'),
]

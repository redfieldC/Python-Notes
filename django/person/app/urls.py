from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('persons/<int:pk>/', views.person_detail, name='person_detail'),
    path('persons/create/', views.create_person, name='create_person'),
    path('persons/update/<int:pk>/', views.update_person, name='update_person'),
    path('persons/delete/<int:pk>/', views.delete_person, name='delete_person'),
]

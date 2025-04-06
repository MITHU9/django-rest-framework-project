from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetail),  # Add this line for detail view
]

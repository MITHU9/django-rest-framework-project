from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetail),

    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),

    path('products/', views.Products.as_view()),
    path('products/<int:pk>/', views.ProductsDetail.as_view()),

    path('todos/', views.Todos.as_view()),
    path('todos/<int:pk>/', views.TodosDetail.as_view()),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
]

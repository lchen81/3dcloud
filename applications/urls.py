from django.urls import path

from . import views


app_name = 'applications'

urlpatterns = [
    path('', views.IndexView.as_view(), name='applications_index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='applications_detail'),
    path('add/', views.add, name='applications_add'),
    path('delete/<int:app_id>/', views.delete, name='applications_delete'),
]

from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('', views.IndexView.as_view(), name='users_index'),
    path('add/', views.add, name='users_add'),
    path('delete/<int:user_id>', views.delete, name='users_delete'),
    path('get_assign_app/<int:user_id>', views.get_assign_app, name='users_get_assign_app'),
    path('put_assign_app/<int:user_id>', views.put_assign_app, name='users_put_assign_app'),
    path('start_app/<int:user_id>/<int:app_id>', views.start_app, name='users_start_app'),
]

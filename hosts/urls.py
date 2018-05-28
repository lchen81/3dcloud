from django.urls import path

from . import views


app_name = 'hosts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='hosts_index'),
    path('add/', views.add, name='hosts_add'),
    path('delete/<int:host_id>', views.delete, name='hosts_delete'),
    path('get_install_app/<int:host_id>', views.get_install_app, name='hosts_get_install_app'),
    path('put_install_app/<int:host_id>', views.put_install_app, name='hosts_put_install_app'),
]

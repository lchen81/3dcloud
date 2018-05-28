from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User
from applications.models import Application
from hosts.models import Host


class IndexView(generic.ListView):
    model = User
    template_name = 'users/index.html'


def add(request):
    if not request.POST['name']:
        return render(request, 'users/index.html', {
            'error_message': "You didn't input the name.",
        })

    u = User(name = request.POST['name'], 
             email = request.POST['email'],
             password = request.POST['password'])
    u.save()

    return HttpResponseRedirect(reverse('users:users_index'))


def delete(request, user_id):
    User.objects.filter(pk=user_id).delete()
    return HttpResponseRedirect(reverse('users:users_index'))


def get_assign_app(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    app_list = Application.objects.all()
    user_app_list = [app.id for app in user.applications.all()]

    return render(request, 'users/assign_app.html', {
        'user': user,
        'app_list': app_list,
        'user_app_list': user_app_list,
    })


def put_assign_app(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    app_list = request.POST.getlist('app_list')

    user.applications.set(app_list)
    user.save()

    return HttpResponseRedirect(reverse('users:users_index'))


def start_app(request, user_id, app_id):
    app = get_object_or_404(Application, pk = app_id)
    
    hosts = ''
    for host in app.host_set.all():
        hosts += host.name + ', '

    if hosts == '':
        return HttpResponse(app.name + ' has not been installed on any host')
    else:
        return HttpResponse(app.name + ' is installed on hosts: ' + hosts)

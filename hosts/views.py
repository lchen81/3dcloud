from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Host
from applications.models import Application


class IndexView(generic.ListView):
    model = Host
    template_name = 'hosts/index.html'


def add(request):
    if not request.POST['name'] or not request.POST['ip']:
        return render(request, 'hosts/index.html', {
            'error_message': "You didn't input the name or ip.",
        })

    h = Host(name = request.POST['name'],
             ip = request.POST['ip'])
    h.save()

    return HttpResponseRedirect(reverse('hosts:hosts_index'))


def delete(request, host_id):
    Host.objects.filter(pk = host_id).delete()
    return HttpRespinseRedirect(reverse('hosts:hosts_index'))


def get_install_app(request, host_id):
    host = get_object_or_404(Host, pk = host_id)
    app_list = Application.objects.all()
    host_app_list = [app.id for app in host.applications.all()]

    return render(request, 'hosts/install_app.html', {
        'host': host,
        'app_list': app_list,
        'host_app_list': host_app_list,
    })


def put_install_app(request, host_id):
    host = get_object_or_404(Host, pk = host_id)
    app_list =  request.POST.getlist('app_list')

    host.applications.set(app_list)
    host.save()

    return HttpResponseRedirect(reverse('hosts:hosts_index'))


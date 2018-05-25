from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Application


class IndexView(generic.ListView):
    model = Application
    template_name = 'applications/index.html'


def add(request):
    if not request.POST['name']:
        return render(request, 'applications/index.html', {
            'error_message': "You didn't input the name.",
        })

    app = Application(name = request.POST['name'],
                      path = request.POST['path'])
    app.save()

    return HttpResponseRedirect(reverse('applications:applications_index'))


def delete(request, app_id):
    Application.objects.filter(pk=app_id).delete()
    return HttpResponseRedirect(reverse('applications:applications_index'))
 

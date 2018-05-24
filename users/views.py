from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User


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

    return HttpResponseRedirect(reverse('users:index'))

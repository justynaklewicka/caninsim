from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Dog
from django.views import generic

def index(request):
    num_dogs = Dog.objects.all().count()
    num_users = User.objects.all().count()

    context = {
        'num_dogs': num_dogs,
        'num_users': num_users,
    }

    return render(request, 'index.html', context=context)

class DogListView(generic.ListView):
    model = Dog
    context_object_name = 'dog_list'
    paginate_by = 10

class DogDetailView(generic.DetailView):
    model = Dog

class UserListView(generic.ListView):
    model = User
    context_object_name = 'user_list'
    paginate_by = 10
    template_name = 'caninsim_app/user_list.html'

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'caninsim_app/user_detail.html'

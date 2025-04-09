from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Dog
from django.views import generic
from django.http import FileResponse
from .utils.image_generator import generate_dog_image_from_genetics

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

def dog_image_view(request, pk):
    dog = Dog.objects.get(pk=pk)
    image_path = f"media/generated_dog_{pk}.png"
    generate_dog_image_from_genetics(dog, image_path)
    return FileResponse(open(image_path, 'rb'), content_type='image/png')

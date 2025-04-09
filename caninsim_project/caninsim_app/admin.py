from django.contrib import admin
from .models import Dog

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'owner', 'gender', 'age', 'size', 'image')
    list_filter = ('gender', 'age', 'size')

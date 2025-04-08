from django.contrib import admin
from .models import Dog

# admin.site.register(Dog)
# Define the admin class
class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'owner', 'gender', 'age', 'size', 'coat')
    list_filter = ('gender', 'age', 'size', 'coat')

# Register the admin class with the associated model
admin.site.register(Dog, DogAdmin)

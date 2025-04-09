from django.db import models
from datetime import datetime as dtm
from django.urls import reverse
import os
from io import BytesIO
from django.core.files.base import ContentFile
from .utils.image_generator import generate_dog_image_from_genetics


class Dog(models.Model):
    SIZES = (
        ('XS', 'miniature'),
        ('S', 'small'),
        ('M', 'medium'),
        ('L', 'big'),
        ('XL', 'huge')
    )

    NOSES = (
        ('BK', 'black'),
        ('LG', 'light gray'),
        ('GR', 'gray'),
        ('AB', 'almost black'),
        ('PL', 'purplish'),
        ('BF', 'butterfly'),
        ('DL', 'dudley'),
        ('SN', 'snow'),
        ('PN', 'pink'),
        ('BP', 'bright pink'),
        ('BR', 'brown'),
    )

    EYES = (
        ('BR', 'brown'),
        ('AM', 'amber'),
        ('LA', 'light brown amber'),
        ('YL', 'yellow'),
        ('YG', 'yellow green'),
        ('GR', 'grey'),
        ('CP', 'copper'),
        ('BL', 'blue'),
        ('AW', 'almost white blue'),
        ('WL', 'wall/heterochromia'),
        ('SP', 'split'),
    )

    COATS = (
        ('HS', 'hairless single heterozygous'),
        ('HL', 'hairless LETHAL homozygous'),
        ('LN', 'long'),
        ('WR', 'wire'),
        ('SM', 'smooth'),
        ('CS', 'curly smooth'),
        ('CL', 'curly long'),
        ('WS', 'wire smooth'),
        ('WL', 'wire long'),
        ('WC', 'wire curly'),
    )

    base_color = models.CharField(max_length=50, choices=[
        ("black", "Black"), ("gold", "Gold"), ("white", "White"),
        ("brown", "Brown"), ("gray", "Gray"),
    ], default="brown")

    marking = models.CharField(max_length=50, choices=[
        ("none", "None"), ("blaze", "Blaze"), ("socks", "Socks"),
        ("patches", "Patches"), ("mask", "Mask"),
    ], default="none")

    creation_date = models.DateTimeField('creation date', default=dtm.now)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    dog_name = models.CharField(max_length=30, default="Unnamed")
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDERS, default='M')
    age = models.IntegerField(default=0)
    size = models.CharField(max_length=150, choices=SIZES, default='M')

    nose = models.CharField(max_length=150, choices=NOSES, default='BK')
    eye = models.CharField(max_length=150, choices=EYES, default='BR')
    # color = models.CharField(max_length=200, null=True)
    coat = models.CharField(max_length=150, choices=COATS, default='SM')

    health_points = models.IntegerField(default=100)
    energy_points = models.IntegerField(default=100)
    hunger = models.IntegerField(default=100)
    thirst = models.IntegerField(default=100)
    bladder = models.IntegerField(default=100)
    exercise = models.IntegerField(default=100)
    exploration = models.IntegerField(default=100)
    social_needs = models.IntegerField(default=100)
    grooming = models.IntegerField(default=100)
    chewing = models.IntegerField(default=100)
    mood = models.IntegerField(default=100)

    active = models.IntegerField(default=5)
    intelligent = models.IntegerField(default=5)
    prey_drive = models.IntegerField(default=5)
    social_skills = models.IntegerField(default=0)

    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.dog_name

    def get_absolute_url(self):
        return reverse("dog_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Generate Pillow image
        image = generate_dog_image_from_genetics(self)

        # Save to in-memory file
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        file_name = f"dog_{self.pk}.png"

        # Save to image field
        self.image.save(file_name, ContentFile(buffer.getvalue()), save=False)
        super().save(update_fields=["image"])

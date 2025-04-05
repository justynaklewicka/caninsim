from django.db import models
from datetime import datetime as dtm


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
    color = models.CharField(max_length=200, null=True)
    coat = models.CharField(max_length=150, choices=COATS, default='SM')

    health_points = models.IntegerField(default=100)
    energy_points = models.IntegerField(default=100)
    hunger = models.IntegerField(default=100)
    thirst = models.IntegerField(default=100)
    bladder = models.IntegerField(default=100)
    exercise = models.IntegerField(default=100)
    exploration = models.IntegerField(default=100)
    social_needs = models.IntegerField(default=100)
    social_skills = models.IntegerField(default=0)
    grooming = models.IntegerField(default=100)
    chewing = models.IntegerField(default=100)
    mood = models.IntegerField(default=100)

    activity = models.IntegerField(default=5)
    intelligent = models.IntegerField(default=5)
    prey_drive = models.IntegerField(default=5)

    def __str__(self):
        return self.dog_name

    # def was_born_recently(self):
    #     return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

# class DogManager(models.Manager):
#     def create_dog(self, dog_name, breed, gender, color, coat, eyes, pigment,
#                    health_points, energy_points, hunger, thirst, bladder, exercise, exploration,
#                    social_needs, social_skills, grooming, chewing, mood
#                    ):
#         dog = self.create(
#             dog_name=dog_name,
#             breed=breed,
#             gender=gender,
#             color=color,
#             coat=coat,
#             eyes=eyes,
#             pigment=pigment,
#
#             # creation_date=today,
#             age=0,
#             health_points=health_points,
#             energy_points=energy_points,
#             hunger=hunger,
#             thirst=thirst,
#             bladder=bladder,
#             exercise=exercise,
#             exploration=exploration,
#             social_needs=social_needs,
#             social_skills=social_skills,
#             grooming=grooming,
#             chewing=chewing,
#             mood=mood
#         )
#         # do something with the dog
#         return dog

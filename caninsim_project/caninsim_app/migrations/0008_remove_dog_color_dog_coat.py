# Generated by Django 5.2 on 2025-04-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caninsim_app', '0007_remove_dog_coat_dog_base_color_dog_image_dog_marking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='color',
        ),
        migrations.AddField(
            model_name='dog',
            name='coat',
            field=models.CharField(choices=[('HS', 'hairless single heterozygous'), ('HL', 'hairless LETHAL homozygous'), ('LN', 'long'), ('WR', 'wire'), ('SM', 'smooth'), ('CS', 'curly smooth'), ('CL', 'curly long'), ('WS', 'wire smooth'), ('WL', 'wire long'), ('WC', 'wire curly')], default='SM', max_length=150),
        ),
    ]

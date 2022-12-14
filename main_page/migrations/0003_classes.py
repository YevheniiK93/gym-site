# Generated by Django 4.1.2 on 2022-10-18 09:08

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_position', models.SmallIntegerField()),
                ('classes_title', models.CharField(max_length=50, verbose_name='Title')),
                ('classes_about', models.TextField(max_length=250, verbose_name='About')),
                ('classes_image', models.ImageField(upload_to=main_page.models.Classes.get_file_name, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Classes',
                'ordering': ('classes_position',),
            },
        ),
    ]

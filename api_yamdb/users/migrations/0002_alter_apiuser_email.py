# Generated by Django 3.2 on 2024-10-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

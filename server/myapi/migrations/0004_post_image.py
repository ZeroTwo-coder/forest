# Generated by Django 4.1.7 on 2023-03-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_delete_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='noimage.png', max_length=300),
        ),
    ]
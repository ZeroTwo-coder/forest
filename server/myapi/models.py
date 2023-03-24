from django.db import models


# class Hero(models.Model):
#     name = models.CharField(max_length=60)
#     alias = models.CharField(max_length=60)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=300, default='noimage.png')

    def __str__(self):
        return self.title

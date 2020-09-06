from django.db import models

class Category(models.Model):
    name = models.CharField("Категорія", max_length=255)
    slug = models.SlugField("Псевдонім", max_length=255, unique=True)

    def __str__(self):
        return self.name


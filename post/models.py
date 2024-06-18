from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    img = models.ImageField(upload_to='authors/', null=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='categories/')

    def __str__(self):
        return f'{self.id}. {self.name}'


class Book(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books/%d-%m-%y')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.id}. {self.name}'



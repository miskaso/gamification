from django.db import models

# Create your models here.


class AboutMe(models.Model):
    name = models.TextField()
    old = models.IntegerField()
    img = models.ImageField()
    description = models.TextField()
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    img = models.ImageField()
    link = models.TextField()

    def __str__(self):
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='images/')


class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

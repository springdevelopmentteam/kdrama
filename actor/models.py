from django.db import models

# Create your models here.
class Actor(models.Model):
    actor_image = models.ImageField()
    actor_name = models.CharField(max_length=255)
    dob = models.DateField()
    zodic_sign = models.CharField(max_length=10)
    drame_name = models.CharField(max_length=255)
    actor_profile = models.TextField()
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.actor_name
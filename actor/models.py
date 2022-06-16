from django.db import models

# Create your models here.
class Zodic(models.Model):
    zodic_sign = models.CharField(max_length=10)

    def __str__(self):
        return self.zodic_sign

class Surname(models.Model):
    surname = models.CharField(max_length=5)

    def __str__(self):
        return self.surname

class DramaName(models.Model):
    drama_name = models.CharField(max_length=255)

    def __str__(self):
        return self.drama_name

class Actor(models.Model):
    actor_image = models.ImageField()
    actor_name = models.CharField(max_length=255)
    surname = models.ForeignKey(Surname, on_delete= models.CASCADE)
    dob = models.DateField()
    zodic_sign = models.ForeignKey(Zodic, on_delete= models.CASCADE)
    drama_name = models.CharField(max_length=255)
    actor_profile = models.TextField()
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.actor_name


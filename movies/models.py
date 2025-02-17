from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    description = models.TextField()
    image_url = models.URLField()
    def __str__(self):
        return str(self.id) + ' ' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key = True)
    comment = models.CharField(max_length = 255)
    date = models.DateTimeField(default = timezone.now)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

class CartItem(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - {self.movie.name} - {self.quantity}'

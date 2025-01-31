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
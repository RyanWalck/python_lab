
from django.db import models

# Create your models here.
class Pokemon(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_pokemon = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Moves(models.Model):

    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="moves")

    def __str__(self):
        return self.title
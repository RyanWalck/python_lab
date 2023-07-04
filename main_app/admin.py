from django.contrib import admin
from .models import Pokemon # import the Artist model from models.py
# Register your models here.

admin.site.register(Pokemon) # this line will add the model to the admin panel
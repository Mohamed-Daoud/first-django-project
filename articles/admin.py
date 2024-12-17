from django.contrib import admin
from .models import Article  # from models.py in the current directory

# Register your models here to show in the admin area
admin.site.register(Article)

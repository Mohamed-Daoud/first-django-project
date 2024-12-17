# All model forms goes here in this file
# Model Form: define a form in Django to be used like signup & login forms

from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta: # define which fields/model to output in this form
        model = models.Article
        fields = ['title', 'slug', 'body', 'thumb', 'myFiles']

from django.db import models
from django.contrib.auth.models import User

# Create your models here; each model (i.e. table) is represented by a class

class Article(models.Model):
    # search for "Field types" in docs.djangoproject.com/.....
    title = models.CharField(max_length = 100) # small number of text
    slug  = models.SlugField()
    body  = models.TextField() # It knows what type of widget to show to users
    date  = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank=True, null=True,
                    upload_to="userImages")
    myFiles = models.FileField(default='my.txt', blank=True, null=True,
                    upload_to="systemFiles")
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



    # show when calling class_name.objects.all() on a shell or in admin site
    def __str__(self):
        return 'Title: "' + self.title + '" --- User: ' + str(self.author)

    def snippet(self):
        return self.body[:50] + '...'

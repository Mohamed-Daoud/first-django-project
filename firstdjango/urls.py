"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views # from current directory import views
# typically for production we do not use the following statement but rather
# use AWS or AWActive serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# follwoing allows us to say where the media url is and where the document root is
# allowing django to serve up those media files
from django.conf.urls.static import static
# follwoing to have access to settings.py file
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='aboutus'), # what to call when making localhost:8000/about
    path('', views.homepage, name = 'home'),  # this is landing page no / needed
    #path('', article_views.articleList, name='home'), # changing the home page
]

# staticfiles_urlpatterns() checks if we are in debug mode then it appends to
# urlpatterns knowing how to server our static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DjangopRestApi
###This is a simple task of Django Restapi. 
###Mainly follow this tutorials: 
###https://wsvincent.com/django-rest-framework-tutorial/

###Environement set up.
###As prerequisit of Django 2 version, We need python 3.5 .
###Main machine: debian 9. 
######
####install django in debian 9
 ###apt-get update && apt-get -y upgrade
 ###apt-get install python3
###apt-get install -y python3-pip
# Create the project directory
 ###mkdir DjangoTest
###cd DjangoTest#
# Create a virtualenv to isolate our package dependencies locally
virtualenv env1
source env1/bin/activate
# Install Django and Django REST framework into the virtualenv

pip3 install Django
pip3 install djangorestframework
#Set up a new project with a single application
django-admin startproject Testapi .
python manage.py startapp posts

############ project set up ###
####Since we’ve added a new app we need to tell Django about it. So make sure to add posts to our list of INSTALLED_APPS in the settings.py file.

# testapi/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'posts',
]

####as the requirements of task  database model will be deliberately quite basic. Let’s create four fields: title, upload (file ), date.

from django.db import models


# posts/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    upload = models.FileField(upload_to='uploads/')
    date = models.DateField()


    def __str__(self):
        return self.title


####Now update  database by first creating a new migration file and then applying it.

 python manage.py makemigrations
 python manage.py migrate
 
 ####
 
 to view  data in Django’s excellent built-in admin app so let’s add Post to it as follows.

# posts/admin.py
from django.contrib import admin
from . models import Post

admin.site.register(Post)

####Then create a superuser account so we can login. Type the command below and enter all the prompts.

 python manage.py createsuperuser
Now we can start up the local web server.

 python manage.py runserver

###Add django framework in settings

add it to the INSTALLED_APPS section of our settings.py file.

# Testapi/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'posts',
]
#######Now create a new serializers.py file in our posts app.

touch posts/serializers.py
Remember that the serializer is used to convert our data into JSON format. That’s it. Here’s what it looks like.

# posts/serializers.py
from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'upload', 'date',)
        model = models.Post
        Next we need to create our views. Just as Django has generic class based views, so too DRF has generic views we can use. Let’s add a view to list all blog posts and a detail view for a specific post.

Update the views.py file in posts as follows.

# posts/views.py
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
##########The final piece is urls. We need to create the url routes–known as endpoints in an API–where the data is available.

Start at the project-level urls.py file.

# Testapi/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]




#######We’ve added include to the second line of imports and then created a path called api/ for our posts app.

Next create our posts app urls.py file.

(blogapi) $ touch posts/urls.py
And then include the code below.

# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

All blog routes will be at api/ so our PostList which has the empty string '' will be at api/ and postDetail at api/# where # represents the primary key of the entry. For example, the first blog post has a primary id of 1 so it will be at the route api/1, the second post at api/2, and so on.

Browsable API
Time to view our work and check out a DRF killer feature. Start up the server.

python manage.py runserver (portnumber)



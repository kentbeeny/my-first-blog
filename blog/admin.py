#from django.contrib import admin

# Register your models here.


#above replaced with lines from tutorial
#
from django.contrib import admin
from .models import Post

admin.site.register(Post)

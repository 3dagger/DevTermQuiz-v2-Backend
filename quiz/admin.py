from django.contrib import admin
from .models import Quiz, VersionCheck

# from .models import Post
# Register your models here.
admin.site.register(Quiz)
admin.site.register(VersionCheck)

from django.contrib import admin
from .models import Posts, CategoryPost, Tags, Comments
# Register your models here.

admin.site.register(Posts)
admin.site.register(CategoryPost)
admin.site.register(Tags)
admin.site.register(Comments)

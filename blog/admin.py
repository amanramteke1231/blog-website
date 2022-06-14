from django.contrib import admin
from .models import Post
from .models import Post, BlogComment

# Register your models here.
admin.site.register((BlogComment))

# we are rigsiter the admin panal

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny.js')
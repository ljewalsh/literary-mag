from django.contrib import admin

from .models import Issue, Author, Story

admin.site.register(Issue)
admin.site.register(Author)
admin.site.register(Story)
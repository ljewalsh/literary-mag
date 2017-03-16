from django.contrib import admin

from .models import Issue, Author, Story, Submitter, Submission


    
admin.site.register(Issue)
admin.site.register(Author)
admin.site.register(Story)
admin.site.register(Submitter)
admin.site.register(Submission)
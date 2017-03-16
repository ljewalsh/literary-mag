from django.contrib import admin

from .models import Issue, Author, Story, Submitter, Submission, About_Text, Submission_Guidelines


    
admin.site.register(Issue)
admin.site.register(Author)
admin.site.register(Story)
admin.site.register(Submitter)
admin.site.register(Submission)
admin.site.register(About_Text)
admin.site.register(Submission_Guidelines)
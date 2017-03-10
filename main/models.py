from __future__ import unicode_literals

from django.db import models

class Issue(models.Model):
    pub_date = models.DateTimeField('date published')
    number = models.IntegerField()
    unpublished = 'Unpublished'
    published = 'Published'
    status_choices = ((unpublished, 'unpublished'), (published, 'published'))
    status = models.CharField(max_length=11, choices=status_choices, default=unpublished)
    
    def __str__(self):
        return "Issue " + str(self.number)
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return name
    
class Story(models.Model):
    issue = models.ForeignKey(Issue),
    author = models.ForeignKey(Author),
    title = models.CharField(max_length=200)

    def __str__(self):
        return title

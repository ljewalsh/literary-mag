from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from froala_editor.fields import FroalaField

def validate_only_one_instance(obj):
	model = obj.__class__
	if (model.objects.count() > 0 and obj.id != model.objects.get().id):
		raise ValidationError("Can only create 1 %s instance" % model.__name__)

class Issue(models.Model):
    pub_date = models.DateTimeField('date published')
    number = models.IntegerField()
    unpublished = 'Unpublished'
    published = 'Published'
    status_choices = ((unpublished, 'unpublished'), (published, 'published'))
    status = models.CharField(max_length=11, choices=status_choices, default=unpublished) 
    cover = models.ImageField(upload_to="covers/", blank=True)
    
    def __str__(self):
        return "Issue " + str(self.number)
        
    @models.permalink
    def get_absolute_url(self):
        return "issue", (str(self.number),)
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Story(models.Model):
    issue = models.ForeignKey(Issue)    
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)
    text = FroalaField(blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "stories"
        
    

class Submitter(models.Model):
    name = models.CharField(max_length=200)
    email =  models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name  
        
class Submission(models.Model):
    title = models.CharField(max_length=200)
    submitter = models.ForeignKey(Submitter)
    file = models.FileField(upload_to="submissions/")
    
    def __str__(self):
        return self.title
        
class About_Text(models.Model):
    text = FroalaField(blank=True)
    
    def clean(self):
        validate_only_one_instance(self)
	
    class Meta:
        verbose_name_plural = "About_Text"
 
class Submission_Guidelines(models.Model):
    text = FroalaField(blank=True)
    
    def clean(self):
        validate_only_one_instance(self)
	
    class Meta:
        verbose_name_plural = "Submission_Guidelines"
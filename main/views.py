from django.shortcuts import render
from .models import Issue, About_Text, Submission_Guidelines

def index(request):    
    if Issue.objects.exists():
        latest_issue = Issue.objects.latest('pub_date')        
    else:
        latest_issue = None
    about_text = About_Text.objects.get(pk='1')    
    return render(request, 'index.html', {'latest_issue': latest_issue, 'about_text': about_text})
    
def journal(request,issue_number, page_number):    
    issue = Issue.objects.get(pk=issue_number)
    stories = issue.story_set.all()   
    story_number = stories.count()    
    return render(request, 'journal.html', {'issue': issue, 'stories': stories, 'page_number':page_number, 'story_number': story_number})
    
def submit(request):
    guidelines = Submission_Guidelines.objects.get(pk='1')
    return render(request, 'submissions.html', {'guidelines':guidelines})
    
def archive(request):
    issues = Issue.objects.all()
    return render(request, 'archive.html', {'issues':issues})

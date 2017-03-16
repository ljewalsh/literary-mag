from django.shortcuts import render
from .models import Issue

def index(request):    
    if Issue.objects.exists():
        latest_issue = Issue.objects.latest('pub_date')        
    else:
        latest_issue = None
    return render(request, 'index.html', {'latest_issue': latest_issue})
    
def journal(request,issue_number, page_number):    
    issue = Issue.objects.get(pk=issue_number)
    stories = issue.story_set.all()   
    story_number = stories.count()    
    return render(request, 'journal.html', {'issue': issue, 'stories': stories, 'page_number':page_number, 'story_number': story_number})
    
def submit(request):
    return render(request, 'submissions.html')
    
def archive(request):
    return render(request, 'archive.html')

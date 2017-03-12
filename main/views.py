from django.shortcuts import render
from .models import Issue

def index(request):    
    if Issue.objects.exists():
        context = {'latest_issue': Issue.objects}
    else:
        context = {'latest_issue': None}
    return render(request, 'index.html', context)
    
def current(request):    
    context = { 
            'latest_issue' : Issue.objects.latest('pub_date')
            }    
    return render(request, 'journal.html', context)
    
def submit(request):
    return render(request, 'submissions.html')
    
def archive(request):
    return render(request, 'archive.html')

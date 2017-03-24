from django.shortcuts import render
from .models import Issue, About_Text, Submission_Guidelines, Submitter, Submission

def get_latest_issue():
    if Issue.objects.exists():
        latest_issue = Issue.objects.filter(status='Published').latest('pub_date')        
    else:
        latest_issue = None
    return latest_issue

def index(request):    
    latest_issue = get_latest_issue()
    about_text = ""
    if About_Text.objects.exists():
        about_text = About_Text.objects.latest('pk')  
    return render(request, 'index.html', {'latest_issue': latest_issue, 'about_text': about_text})
    
def journal(request,issue_number, page_number):    
    issue = Issue.objects.get(pk=issue_number)
    stories = issue.story_set.all()   
    story_number = stories.count()    
    return render(request, 'journal.html', {'issue': issue, 'stories': stories, 'page_number':page_number, 'story_number': story_number})
    
def submit(request):
    latest_issue = get_latest_issue()
    guidelines = ""
    if Submission_Guidelines.objects.exists():
        guidelines = Submission_Guidelines.objects.latest('pk')
    return render(request, 'submissions.html', {'latest_issue': latest_issue,'guidelines':guidelines})
    
def archive(request):
    latest_issue = get_latest_issue()
    issues = Issue.objects.filter(status='Published')
    return render(request, 'archive.html', {'latest_issue': latest_issue,'issues':issues})
	
def submitting(request):
    latest_issue = get_latest_issue()
    guidelines = ""
    if Submission_Guidelines.objects.exists():
        guidelines = Submission_Guidelines.objects.latest('pk')
    thetitle = request.POST['title']
    thename = request.POST['name']
    theemail = request.POST['email']
    thefile = request.POST['file']
    error = None
    try:
        if Submitter.objects.filter(email=theemail).exists():
            thesubmitter = Submitter.objects.filter(email=theemail)
        else:
            thesubmitter = Submitter.objects.create(name=thename, email=theemail)
        Submission.objects.create(title=thetitle, submitter=thesubmitter, file=thefile)
        error = "Your submission has been accepted"
    except Exception:
        error = "Something went wrong, make sure you included all fields correctly"
    return render(request, 'submissions.html', {'latest_issue': latest_issue,'guidelines':guidelines,'error':error})

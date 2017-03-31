from django.shortcuts import render
from .models import Issue, About_Text, Submission_Guidelines, Submitter, Submission
from .forms import SubmitForm

def get_latest_issue():
    try:
        latest_issue = Issue.objects.filter(status='Published').latest('pub_date')
    except:
        latest_issue = None
    return latest_issue

def index(request):    
    latest_issue = get_latest_issue()
    about_text = ""
    if About_Text.objects.exists():
        about_text = About_Text.objects.latest('pk')  
    issue_count = Issue.objects.filter(status='Published').count()
    return render(request, 'index.html', {'latest_issue': latest_issue, 'about_text': about_text, 'issue_count': issue_count})
    
def journal(request,issue_number, page_number):    
    issue = Issue.objects.get(number=issue_number)
    stories = issue.story_set.all()   
    story_number = stories.count()    
    latest_issue = get_latest_issue()
    issue_count = Issue.objects.filter(status='Published').count()
    return render(request, 'journal.html', {'issue': issue, 'latest_issue': latest_issue, 'stories': stories, 'page_number':page_number, 'story_number': story_number, 'issue_count': issue_count})
    
def submit(request):
    latest_issue = get_latest_issue()
    guidelines = ""
    if Submission_Guidelines.objects.exists():
        guidelines = Submission_Guidelines.objects.latest('pk')
    issue_count = Issue.objects.filter(status='Published').count()
    return render(request, 'submissions.html', {'latest_issue': latest_issue,'guidelines':guidelines, 'issue_count': issue_count, 'form': SubmitForm})
    
def archive(request):
    latest_issue = get_latest_issue()
    issues = Issue.objects.filter(status='Published')
    return render(request, 'archive.html', {'latest_issue': latest_issue,'issues':issues})
	
def submitting(request):
    latest_issue = get_latest_issue()
    guidelines = ""
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('submit')
    else:
        form = SubmitForm()
    return render(request, 'submissions.html', {'latest_issue': latest_issue,'guidelines':guidelines,'error':error})

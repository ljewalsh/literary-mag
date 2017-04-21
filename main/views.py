from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
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
    try:
        issue = Issue.objects.get(number=issue_number)
    except:
        raise Http404("Issue number "+issue_number+" does not exist.")
    if issue.status != 'Published':
		raise Http404("Issue number "+issue_number+" is not currently published.")
    stories = issue.story_set.all()   
    story_number = stories.count()    
    if int(page_number) > story_number or int(page_number) < 0:
        raise Http404("Issue number "+issue_number+" does not have "+page_number+" pages.")
    latest_issue = get_latest_issue()
    issue_count = Issue.objects.filter(status='Published').count()
    return render(request, 'journal.html', {'issue': issue, 'latest_issue': latest_issue, 'stories': stories, 'page_number':page_number, 'story_number': story_number, 'issue_count': issue_count})
    
def submit(request):
    latest_issue = get_latest_issue()
    guidelines = ""
    if Submission_Guidelines.objects.exists():
        guidelines = Submission_Guidelines.objects.latest('pk')
    issue_count = Issue.objects.filter(status='Published').count()
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            sub = request.POST
            try:
                submitter = Submitter.objects.filter(email=sub['email']).latest('pk')
            except:
                submitter = Submitter.objects.create(name=sub['name'], email=sub['email'])
            submit = Submission.objects.create(title=sub['title'], submitter=submitter, file=request.FILES['file'])
            messages.success(request, 'Your story has been submitted for review. Thank you for your contribution')
            return HttpResponseRedirect('submit')
    else:
        form = SubmitForm()
    return render(request, 'submissions.html', {'latest_issue': latest_issue,'guidelines':guidelines, 'issue_count': issue_count, 'form': form})
    
def archive(request):
    latest_issue = get_latest_issue()
    issues = Issue.objects.filter(status='Published')
    issue_count = Issue.objects.filter(status='Published').count()
    return render(request, 'archive.html', {'latest_issue': latest_issue, 'issues':issues, 'issue_count':issue_count})

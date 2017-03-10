from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
    
def current(request):
    return render(request, 'journal.html')
    
def submit(request):
    return render(request, 'submissions.html')
    
def archive(request):
    return render(request, 'archive.html')

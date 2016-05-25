from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import userForm

# Create your views here.
@login_required(login_url='/resume/login/')
def success(request):
    return render(request, 'resume_mgmt/index.html')

@login_required(login_url='/resume/login/')
def create(request):
    return render(request, "resume_mgmt/create.html")

@login_required(login_url='/resume/login/')
def edit(request):
    return render(request, 'resume_mgmt/edit.html')

@login_required(login_url='/resume/login/')
def query(request):
    return render(request, 'resume_mgmt/query.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext, redirect
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from django.views import generic
from .models import Resume
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Create your views here.
@login_required(login_url='/resume/login/')
def success(request):
    return render(request, 'resume_mgmt/index.html')

@login_required(login_url='/resume/login/')
def edit(request):
    return render(request, 'resume_mgmt/edit.html')

#@login_required(login_url='/resume/login/')
class Query(generic.DetailView):
    model = Resume
    template_name = 'resume_mgmt/querydetail.html'

class QueryView(generic.ListView):
    template_name = 'resume_mgmt/query.html'
    context_object_name = 'resumelist'

    def get_queryset(self):
        if self.request.GET.get("sort"):
            return Resume.objects.all().order_by(self.request.GET.get("sort"))
        else:
            return Resume.objects.all()

def sorts(request):
    if request.GET.get("sort_name"):
        return Resume.objects.order_by("name")


@login_required(login_url='/resume/login/')
def test(request):
        form = ResumeForm(request.POST or None)
        if form.is_valid():
            saveit= form.save(commit=False)
            saveit.save()
            return HttpResponseRedirect("/resume/query")

        return render_to_response("resume_mgmt/test.html", locals(), context_instance=RequestContext(request))

def edit(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/resume/query', pk=post.pk)
    else:
        form = ResumeForm(instance=post)

    return render_to_response("resume_mgmt/edit.html", locals(), context_instance=RequestContext(request))
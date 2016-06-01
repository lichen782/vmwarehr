from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext, redirect
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from django.views import generic
from .models import Resume
from django.db.models import Q
import operator
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
        resume_list = Resume.objects.all()

        query = self.request.GET.get('search')
        if query:
            filtered_list = resume_list.filter(Q(name__istartswith=query) |
                                      Q(age__icontains=query))
            return filtered_list

        if self.request.GET.get("sort"):
            global filtered_list
            return filtered_list.order_by(self.request.GET.get("sort"))
        else:
            return resume_list

class SearchResultsView(generic.ListView):
    template_name = 'resume_mgmt/query.html'
    context_object_name = 'searchlist'

    def get_queryset(self):
        q = self.request.GET['q']
        return Resume.objects.filter(name__search=q)


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

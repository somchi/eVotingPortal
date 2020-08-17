from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from candidates.models import Candidate, Category

def Homepage(request):
    return render(request, 'homepage/base_site.html')

class category(generic.ListView):
    model = Category
    template_name = 'homepage/base_site.html'
    context_object_name = 'category_list'



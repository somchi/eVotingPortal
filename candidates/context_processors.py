from .models import Category
from django.shortcuts import render
from django.template import RequestContext, loader

def context(request):
   category_lists = Category.objects.all()
   context = {'category_lists': category_lists}
   return context

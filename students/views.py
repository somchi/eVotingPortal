from django.shortcuts import render
from .context_processors import Registration
from django.views import generic
from .models import RegistrationForm
from django.http import HttpResponseRedirect

def Register(request):
    form = Registration(request.POST or None)
    #if request.method == 'POST':
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/students/Locatio/")
    else:
        form = Registration()
    context = {
        "form": form
    }
    return render(request, "students/index.html", context)
class LocationChange(generic.ListView):
    model = RegistrationForm
    template_name = 'students/NewLocation.html'

def Registratio(request):
    return render(request, 'students/register.html')
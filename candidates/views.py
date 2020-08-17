from django.shortcuts import render
from django.views import generic
from .models import Candidate, Category, RegistrationForm
from .forms import Registration
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.auth import authenticate, login
from django.template import loader, RequestContext
from django.contrib import messages
from django.contrib.auth import logout

def Student_Registration(request):
    return render(request, 'candidates/register.html')

class VoteSpot(generic.DetailView):
    model = RegistrationForm
    template_name = 'candidates/VoteArena.html'

class IndexView(generic.ListView):
    model = Category
    template_name = 'candidates/candidate.html'
    context_object_name = 'category_list'

class DetailView(generic.DetailView):
    model = Category
    template_name = 'candidates/category.html'

class CandidateView(generic.DetailView):
    model = Candidate
    template_name = 'candidates/candidates_detail.html'

def Register(request):
    form = Registration(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.image = request.FILES['image']
        instance.save()
        messages.success(request, "You have successfully created an account")
        return HttpResponseRedirect('/candidates/%i/location/' % instance.pk)
    else:
        form = Registration()
    context = {
        "form": form
    }
    return render(request, "candidates/student_registration.html", context)

def election_vote(request, candidate_category_id ):
    category = get_object_or_404(Category, pk=candidate_category_id )
    try:
        selected_candidate = category.candidate_set.get(pk=request.POST['candidate'])
    except (KeyError, Candidate.DoesNotExist):
        return render(request, 'candidates/category.html', {'category': category, 'error_message': "You didn't select a choice"})
    else:
        selected_candidate.candidate_vote = F('candidate_vote')+1
        selected_candidate.save()
        return HttpResponseRedirect(reverse('election_result'))

class election_result(generic.ListView):
    model = Category
    template_name = 'candidates/election_result.html'

def Authentications(request):
    m = RegistrationForm.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['student_id'] = m.id
        return HttpResponseRedirect('/candidates/%i/location/' % m.pk)
    else:
        messages.error(request, 'Incorrect login details')
        return HttpResponseRedirect(reverse('StudentLog'))


class StudetUpdate(generic.UpdateView):
    model = RegistrationForm
    form_class = Registration
    template_name= 'candidates/student_update_form.html'
    success_url = 'register'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, "You have successfully edited ur profile")
        return HttpResponseRedirect('/candidates/%i/location/' % self.object.pk)
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('StudentLog'))

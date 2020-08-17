from django.contrib import admin
from candidates.models import Candidate, Category, RegistrationForm
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_first_name', 'candidate_surname', 'candidate_image', 'candidate_category')

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Category)
admin.site.register(RegistrationForm)



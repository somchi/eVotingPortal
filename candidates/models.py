from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image
from django.contrib.auth.models import User

class Category(models.Model):
    CategoryPo = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryPo

class Candidate(models.Model):
    candidate_first_name = models.CharField(max_length=100, verbose_name='First Name')
    candidate_surname = models.CharField(max_length=100)
    candidate_goal = models.TextField()
    candidate_image = models.ImageField(upload_to='images')
    candidate_vote = models.BigIntegerField()
    candidate_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate_first_name
        return self.candidate_surname

class RegistrationForm(models.Model):
    LEVELS = (
        ('first', '100 Level'),
        ('second', '200 Level'),
        ('third', '300 Level'),
        ('forth', '400 Level'),
    )

    first_name = models.CharField(verbose_name='First Name', max_length=200, help_text='100 character maximum')
    last_name = models.CharField(verbose_name='Last Name', max_length=200)
    reg_no = models.IntegerField(verbose_name='Reg Number')
    image = models.ImageField(upload_to='images', blank=True)
    date_of_birth = models.DateField(verbose_name='DOB')
    level = models.CharField(max_length=100, choices=LEVELS)
    institution = models.CharField(max_length=200)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=10)

    class Meta:
        permissions = ("can_vote", "Can Vote"),

    def __str__(self):
        return self.first_name
        return self.last_name

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


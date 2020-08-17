from __future__ import unicode_literals
from django.db import models

# Create you
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
    date_of_birth = models.DateField(verbose_name='DOB')
    level = models.CharField(max_length=100, choices=LEVELS)
    institution = models.CharField(max_length=200)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
        return self.last_name
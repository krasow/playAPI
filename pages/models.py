from django.db import models
from phone_field import PhoneField

class PhoneModel(models.Model):
    to = models.CharField(max_length=12,blank=True, help_text='Enter phone number')

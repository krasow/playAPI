from django.db import models

class PhoneModel(models.Model):
    to = models.CharField(max_length=12,blank=False, help_text='Enter phone number')
    sid = models.CharField(max_length=100,blank=False)
    code = models.CharField(max_length=12,blank=False, help_text='Enter Verification Code')
    def __str__(self):
        return self.to

from django.db import models
from django.contrib.auth.models import *
from datetime import date
from django.conf import settings

# Create your models here.
ACCEPTED_FORMATS = ['%Y-%m-%d']
class Manufacture(models.Model):
    # created_by = models.IntegerField()
    # created_date = models.DateTimeField(auto_now_add=True, editable=False)
    CHOICES = (
        ('select1', 'All Weather'),
        ('select2', 'Aggressive'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(ACCEPTED_FORMATS)
    end_date = models.DateField(ACCEPTED_FORMATS)
    warehouse1 = models.CharField(max_length=250, blank=True)
    store1 = models.CharField(max_length=100, blank=True)
    warehouse2 = models.CharField(max_length=250, blank=True)
    store2 = models.CharField(max_length=100, blank=True)
    warehouse3 = models.CharField(max_length=250, blank=True)
    store3 = models.CharField(max_length=100, blank=True)
    warehouse4 = models.CharField(max_length=250, blank=True)
    store4 = models.CharField(max_length=100, blank=True)
    warehouse5 = models.CharField(max_length=250, blank=True)
    store5 = models.CharField(max_length=100, blank=True)
    warehouse6 = models.CharField(max_length=250, blank=True)
    store6 = models.CharField(max_length=100, blank=True)
    warehouse7 = models.CharField(max_length=250, blank=True)
    store7 = models.CharField(max_length=100, blank=True)
    warehouse8 = models.CharField(max_length=250, blank=True)
    store8 = models.CharField(max_length=100, blank=True)
    warehouse9 = models.CharField(max_length=250, blank=True)
    store9 = models.CharField(max_length=100, blank=True)
    warehouse10 = models.CharField(max_length=250, blank=True)                      
    store10 = models.CharField(max_length=100, blank=True)
    warehouse11 = models.CharField(max_length=250, blank=True)                      
    store11 = models.CharField(max_length=100, blank=True)
    warehouse12 = models.CharField(max_length=250, blank=True)                      
    store12 = models.CharField(max_length=100, blank=True)
    warehouse13 = models.CharField(max_length=250, blank=True)                      
    store13 = models.CharField(max_length=100, blank=True)
    warehouse14 = models.CharField(max_length=250, blank=True)                      
    store14 = models.CharField(max_length=100, blank=True)
    warehouse15 = models.CharField(max_length=250, blank=True)                      
    store15 = models.CharField(max_length=100, blank=True)
    like = models.CharField(max_length=50, choices=CHOICES)
    

    

  
    #def get_absolute_url(self):
     #    return reverse('music:album-update', kwargs={'pk': self.pk})

    
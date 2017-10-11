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
    store1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse2 = models.CharField(max_length=250, blank=True)
    store2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse3 = models.CharField(max_length=250, blank=True)
    store3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse4 = models.CharField(max_length=250, blank=True)
    store4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse5 = models.CharField(max_length=250, blank=True)
    store5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse6 = models.CharField(max_length=250, blank=True)
    store6 = models.DecimalField(max_digits=5, decimal_places=2, default=100, null=True)
    warehouse7 = models.CharField(max_length=250, blank=True)
    store7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse8 = models.CharField(max_length=250, blank=True)
    store8 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse9 = models.CharField(max_length=250, blank=True)
    store9 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse10 = models.CharField(max_length=250, blank=True)                      
    store10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse11 = models.CharField(max_length=250, blank=True)                      
    store11 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse12 = models.CharField(max_length=250, blank=True)                      
    store12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse13 = models.CharField(max_length=250, blank=True)                      
    store13 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse14 = models.CharField(max_length=250, blank=True)                      
    store14 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    warehouse15 = models.CharField(max_length=250, blank=True)                      
    store15 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=100)
    like = models.CharField(max_length=50, choices=CHOICES)
    

    

  
    #def get_absolute_url(self):
     #    return reverse('music:album-update', kwargs={'pk': self.pk})

    
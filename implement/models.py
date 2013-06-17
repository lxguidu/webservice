# encoding: utf-8

from django.db import models

# Create your models here.
class AccessToken(models.Model):
    token = models.CharField('Token', max_length=100)
    
    def __unicode__(self):
        return 'Token: %s' % self.token
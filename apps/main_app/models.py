# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..log_app.models import User

class PlayManger(models.Manager):
    def addVal(self, postData): # validates login
        results = {'errors':[], 'status': False, 'user': None} # empty dictionary with keys 'errors' and 'user'
        
        if len(postData['title']) < 2:
            results['status'] = True
            results['errors'].append('Title is too short.')

        if not postData['title'].isalnum():
            results['status'] = True
            results['errors'].append('Title, please use alphanumeric characters')

        if len(postData['artist']) < 2:
            results['status'] = True
            results['errors'].append('Artist is too short.')

        if not postData['artist'].isalnum():
            results['status'] = True
            results['errors'].append('Artist, please use alphanumeric characters')
        return results


# Create your models here.
class Play(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User,related_name="playlists")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlayManger()

    

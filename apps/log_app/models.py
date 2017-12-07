from __future__ import unicode_literals
from django.db import models
import re
import bcrypt




class UserManger(models.Manager):
    
    def loginVal(self, postData): # validates login
        results = {'errors':[], 'status': False, 'user': None} # empty dictionary with keys 'errors' and 'user'
        email_matches = self.filter(email = postData['email']) # filters the user with the same email address
        if len(email_matches) == 0: 
            results['errors'].append('Please check your email and password and try again')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your email and password and try again')
                results['status'] = True
        return results

        

    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        return self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'],password = password)
        

    
        

        

    def registerVal(self, postData):
        results = {'errors':[], 'status': False}

        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short.')

        if not postData['first_name'].isalnum():
            results['status'] = True
            results['errors'].append('First name, please use alphanumeric characters')

        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short.')
        
        if not postData['last_name'].isalnum():
            results['status'] = True
            results['errors'].append('Last name, please use alphanumeric characters')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = True
            results['errors'].append('Email is not valid')

        if len(postData['password']) < 3:
            results['status'] = True
            results['errors'].append('Password is too short.')
        
        if not postData['password'].isalnum():
            results['status'] = True
            results['errors'].append('Password is too short.')

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match.')

        user = self.filter(email= postData['email'])

        if len(user) > 0:
            results['status'] = True
            results['errors'].append('User already exists in database.')

        return results
         
    # def contains_alphanumeric( email):
    #     r=re.match('[0-9a-zA-Z]+', email)
    #     if r==None:
    #      return False
    #     else:
    #      return True
    

class User(models.Model):
    first_name = models.CharField(max_length = 250) # user first name
    last_name = models.CharField(max_length = 250) # user last name
    email = models.CharField(max_length = 250) # user email
    password = models.CharField(max_length = 250) # user password
    # friends = models.ManyToManyField('User')
    objects = UserManger() # this is for validation


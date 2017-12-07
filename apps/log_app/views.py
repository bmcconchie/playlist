# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
# from datetime import date

def logout(request): # logs out 
    request.session.flush() # clears out of session 
    return redirect ('/') # redirects to root route

def index(request): # renders the login/registration page
    return render(request, 'log_app/index.html') 

def register(request): # create user
    results = User.objects.registerVal(request.POST) # returns dictionary with error message and user
    if results['status'] == False: # if no error message
        user = User.objects.createUser(request.POST)
        messages.success(request, "Your user has been created. Please login") # creates a flash message
        request.session['first_name'] = user.first_name 
        request.session['id'] = user.id
        request.session['email'] = user.email
    else: # if there are any errors
        for error in results['errors']:  # error message
            messages.error(request, error)
    return redirect('/main/') # redirects to main page if error

def login(request):
    results = User.objects.loginVal(request.POST) # returns dictionary with error message and user
    if results['status'] == True: # if there are any error 
        for error in results['errors']: # error message
            messages.error(request, error)
        return redirect('/') # redirects to main page if error
    else: # if no error message
        request.session['first_name'] = results['user'].first_name
        request.session['id'] = results['user'].id
        request.session['email'] = results['user'].email
        return redirect('/main/') # redirects to login page

# def calculate_age(born):
#     today = date.today()
#     try: 
#         birthday = born.replace(year=today.year)
#     except ValueError: # raised when birth date is February 29 and the current year is not a leap year
#         birthday = born.replace(year=today.year, month=born.month+1, day=1)
#     if birthday > today:
#         return today.year - born.year - 1
#     else:
#         return today.year - born.year 

# d = datetime.date(2013, 1, 1)
# print(d)
# year, month, day = map(int, d.split('-'))
# d = datetime.date(year, month, day)
# d = dplanted.strftime('%m/%d/%Y')
# d = datetime.date(d)+timedelta(days=30)
# print(d)
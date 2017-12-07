# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Play
from ..log_app.models import User
from django.contrib import messages


def main(request):
    if 'first_name' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    # count = user.count.values("add").annotate(num_of_add)
    context = {
        'playlists' : Play.objects.all(),
        'user' : user
        
    }
    return render(request, 'main_app/main.html', context)

def songUser(request, id):
    if 'first_name' not in request.session:
        return redirect('/')
    other_users = Play.objects.get(id=id).users.exclude(id=Play.objects.get(id=id).users.get(id=request.session['id']).id)
    times = {}
    for user in other_users:
        times[str(user.id)] = user.playlists.all().filter(id=id).count()
        print user.playlists.all().filter(id=id).count()

    print times    
    context = {
        'playlist' : Play.objects.get(id=id),
        'other_users' : other_users,
        'times' : times
        
    }
    return render(request, 'main_app/song.html', context)

def create(request):
    if 'first_name' not in request.session:
        return redirect('/')
    results = Play.objects.addVal(request.POST)
    if results['status']: 
        for error in results['errors']:  # error message
            messages.error(request, error)
        return redirect('/main')
    playlist = Play.objects.create(title = request.POST['title'], artist = request.POST['artist'])
    playlist.users.add(User.objects.get(id=request.session['id']))
    return redirect('/main')



def add(request, id):
    if 'first_name' not in request.session:
        return redirect('/')
    
    user = User.objects.get(id=request.session['id'])
    user.playlists.add(Play.objects.get(id=id))
    return redirect('/main')
    
def showUser(request, id):
    if 'first_name' not in request.session:
        return redirect('/')

    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request, 'main_app/show.html', context)

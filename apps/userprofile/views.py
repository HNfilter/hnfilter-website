from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username): # SMA: required login ??
    user = get_object_or_404(User, username=username)

    # total number of votes this user has received
    number_of_votes = 0
    for item in user.items.all():
        number_of_votes = number_of_votes + (item.number_of_votes)

    context = {
        'user': user,
        'number_of_votes': number_of_votes,
    }
    return render(request, 'userprofile/userprofile.html', context)

def votes(request, username): # SMA: required login ??
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    items = []

    for vote in votes:
        items.append(vote.item)

    context = {
        'user': user,
        'items': items,
    }
    return render(request, 'userprofile/votes.html', context)

def submissions(request, username):
    user = get_object_or_404(User, username=username)
    items = user.items.all()

    context = {
        'user': user,
        'items': items,
    }
    return render(request, 'userprofile/submissions.html', context)

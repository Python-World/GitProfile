from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api.GitUser import GitUser

# Create your views here.


def index(request):
    return render(request, 'index.html')


def get_profile(request, username):
    if request.method == 'GET':
        user_data = GitUser(username)
        return render(request, 'dashboard.html', {'data': user_data})
    else:
        return render(request, 'index.html')


def get_overview(request, username):
    user_data = GitUser(username)
    data = user_data.get_overview()
    return JsonResponse(data={
        'labels': list(data.keys()),
        'data': list(data.values()),
    })


def get_languages(request, username):
    user_data = GitUser(username)
    data = user_data.get_languages()
    return JsonResponse(data={
        'labels': list(data.keys()),
        'data': list(data.values()),
    })


def get_all_data(request, username):
    user_data = GitUser(username)
    overview = user_data.get_overview()
    details = {
        'Followers': user_data.followers,
        'Following': user_data.following,
        'Repos': user_data.repos,
        'Gists': user_data.gist,
        **overview
    }
    return JsonResponse(data={
        'labels': list(details.keys()),
        'data': list(details.values()),
        'username': user_data.username
    })

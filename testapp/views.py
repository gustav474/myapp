from django.shortcuts import render
import requests

client_id = 6689761
redirect_uri = 'http://gusstav474.pythonanywhere.com/redirect'
display = 'page'
scope = 'friends'
response_type = 'token'
v = 5.84

def index(request):
    access_token = request.GET['access_token']
    user_id = request.GET['user_id']

    payloads = {'user_id': user_id, 'access_token': access_token, 'order': 'random', 'fields': 'nickname',
                    'count': 5, 'v': v}
    response = requests.get('https://api.vk.com/method/friends.get', params=payloads)
    friends = response.json()['response']['items']

    return render(request, 'test/index.html', {'friends': friends})

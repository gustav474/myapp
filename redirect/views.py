from django.shortcuts import render

# client_id = 6689761
# redirect_uri = 'http://gusstav474.pythonanywhere.com/redirect'
# display = 'page'
# scope = 'friends'
# response_type = 'token'
# v = 5.84

def index(request):
    return render(request, 'redirect/index.html')



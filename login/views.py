from django.shortcuts import render
from django.shortcuts import redirect
# from vkoauth import VKOauth
from django.http import HttpResponse
from urllib.parse import parse_qs, urlparse
import requests
from bs4 import BeautifulSoup

client_id = 6689761
redirect_uri = 'http://gusstav474.pythonanywhere.com/redirect'
display = 'page'
scope = 'friends'
response_type = 'token'
v = 5.84

login = 'yana_luda@orel.ru'
password = '!Orange25'

payloads = {'client_id': client_id, 'redirect_uri': redirect_uri,
            'display': display, 'scope': scope, 'response_type': response_type, 'v': v}

class VKOauth():
    def __init__(self, client_id, redirect_uri, display, scope, response_type, v):
        self.session = requests.Session()
        self.is_autorized = False

        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.display = display
        self.scope = scope
        self.response_type = response_type
        self.v = v

        self.user_id = None
        self.access_token = None
        # self.response = None

    def get_title(self):
        soup = BeautifulSoup(self.response1.text, features="html.parser")
        title = soup.title.string
        return title

    def autorize(self):
        url = 'https://oauth.vk.com/authorize'

        payloads = {'client_id': self.client_id, 'redirect_uri': self.redirect_uri,
                    'display': self.display, 'scope': self.scope, 'response_type': self.response_type, 'v': self.v}

        # Запрос на авторизацию
        self.response1 = self.session.get(url, params=payloads)

        return self.response1.url

        # Если мы не авторизованы
        # if True:
        #     return redirect(self.response1.url)


        # if VKOauth.get_title(self) == 'Получение доступа к ВКонтакте':
        #
        #     soup = BeautifulSoup(self.response1.text, features="html.parser")
        #
        #     form_action_auth = soup.form['action']
        #     input_to = soup.form.find(name='input', attrs={'name': 'to'})['value']
        #     input_origin = soup.form.find(name='input', attrs={'name': '_origin'})['value']
        #     input_ip_h = soup.form.find(name='input', attrs={'name': 'ip_h'})['value']
        #     input_lg_h = soup.form.find(name='input', attrs={'name': 'lg_h'})['value']
        #
        #     data_auth = {'to': input_to, '_origin': input_origin, 'ip_h': input_ip_h, 'lg_h': input_lg_h, 'email': login,
        #                  'pass': password}
        #
        #     # Логин/пароль (разрешаем приложению доступ к данным аккаунта вк)
        #     self.response2 = self.session.post(form_action_auth, data=data_auth)
        #
        #     # Get fragment params
        #     # self.access_token = parse_qs(urlparse(self.response2.url).fragment)['access_token']
        #     # self.expires_in = parse_qs(urlparse(self.response2.url).fragment)['expires_in']
        #     # self.user_id = parse_qs(urlparse(self.response2.url).fragment)['user_id']

        # return self.response1.text

    # def get_friends(self):
    #     payloads = {'user_id': self.user_id, 'access_token': self.access_token, 'order': 'random', 'fields': 'nickname',
    #                 'count': 5, 'v': v}
    #     response = self.session.get('https://api.vk.com/method/friends.get', params=payloads)
    #
    #     return response.text


def index(request):

    vkoauth = VKOauth(client_id, redirect_uri, display, scope, response_type, v)

    # vkoauth.autorize()

    return redirect(vkoauth.autorize())

    # return render(request, 'test/index.html', {'inputs': vkoauth.response2.text})

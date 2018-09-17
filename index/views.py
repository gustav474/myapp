from django.shortcuts import render
from urllib.parse import parse_qs, urlparse
from django.template import RequestContext

def index(request):
    data = request.get_full_path
    # access_token = urlparse(request.build_absolute_uri)
    return render(request, 'index/index.html')

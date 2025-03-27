from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# dev_1
def home(request):
    context = {'message': 'Hello, Django!'}
    return render(request, 'store/home.html', context )
    # return HttpResponse("<h1>이제부터 쇼핑몰을 만들어 봅시다.</h1>")

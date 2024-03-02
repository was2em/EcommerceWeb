from django.shortcuts import render
from ShoppingCart.settings import BASE_DIR
# Create your views here.


def login(request):
    return render(request, 'index.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# dev_26
@login_requiredequired(login_url="accounts:login_user")
def payment_process(request):
    pass
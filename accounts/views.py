from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.forms import RegisterUserForm # 절대 경로 형식

# Create your views here.

# class HTTPRequest:
#    POST = {"username":"admim","password":"1234"}
#    GET = {}

# dev_9

def logout_user(request):
    logout(request) # session에 저장된 sessionid 삭제
    return redirect("/")

def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in")
            return redirect("/")
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect("accounts:login_user")
    else:
        return render(request, "accounts/login.html", {})

# dev_10
def register_user(request):

    form = RegisterUserForm()

    if request.method == "POST":
        print(form)
        # username = request.POST["username"]
        # password = request.POST["password"]
        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "You Have been logged in")
        #     return redirect("/")
        # else:
        #     messages.success(request, ("There was an error, please try again"))
        #     return redirect("accounts:login_user")
    else:
        context = {"form":form}

    return render(request, "accounts/register.html", context)
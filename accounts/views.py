from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# from .forms import RegisterUserForm # 상대 경로형식
from accounts.forms import RegisterUserForm  # 절대 경로 형식

# Create your views here.

# class HTTPRequest:
#    POST = {"username":"admim","password":"1234"}
#    GET = {}
# dev_9


def logout_user(request):
    logout(request)  # session 에 저장된 sessionid 삭제
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
# dev_11 회원가입 로직
def register_user(request):

    if request.method == "POST":

        if request.POST["password1"] == request.POST["password2"]:
            form = RegisterUserForm(request.POST)  # 모델에 다가 값을 넣음

            if form.is_valid():
                form.save()  # 회원 DB 저장

                # 회원가입 하자 마자, 로그인 시켜줌
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")

                user = authenticate(username=username, password=raw_password)
                login(request, user)

                return redirect("/")

    else:
        form = RegisterUserForm()

    return render(request, "accounts/register.html", {"form": form})
from django.shortcuts import render,redirect
from django.contrib import auth
import webbrowser


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    else:
        return render(request, 'login2.html')
    
def logout(request):
    auth.logout(request)
    url="https://accounts.kakao.com/logout?continue=https://accounts.kakao.com/weblogin/account"
    webbrowser.open(url)
    return redirect('home')


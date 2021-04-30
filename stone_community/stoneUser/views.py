from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import stoneUser

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data ={}
        if not (username and password and re_password) :
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'

        else:
            stoneuser = stoneUser(
            username = username,
            password = make_password(password)
            )
            stoneuser.save()

        return render(request, 'register.html', res_data)

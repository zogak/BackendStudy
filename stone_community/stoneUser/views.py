from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import stoneUser

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        stoneuser = stoneUser.objects.get(pk=user_id)
        return HttpResponse(stoneuser.username)

    return HttpResponse('home!')
    
def login(request):
    if request.method == 'GET': #request가 get으로 들어온 경우
        return render(request, 'login.html') #화면 그냥 보여줌
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        res_data = {}
        if not (username and password): #값을 모두 입력하지 않았을 시
            res_data['error'] = '모든 값을 입력해야 합니다.'
        
        else:
            stoneuser = stoneUser.objects.get(username = username)
            if check_password(password, stoneuser.password):
                request.session['user'] = stoneuser.id
                return redirect('/')

            else: #비번 틀림
                res_data['error'] = '비밀번호가 틀렸습니다.'
        return render(request, 'login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
    
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None) #template의 id랑 같아야함

        res_data ={}

        if not (username and password and re_password):
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

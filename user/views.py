from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        pasword = request.POST.get('password',None)
        pasword2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)
        
        
        if pasword != pasword2:
            return render(request,'user/signup.html')
        else:
            exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html') #사용자 존재 있으면 나타나는 페이지 
            else:
                new_user = UserModel()
                new_user.username =username
                new_user.password =pasword
                new_user.password =pasword2
                new_user.bio =bio
                new_user.save()
                return redirect('/sign-in/')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password  = request.POST.get('password',None)
        
        
        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return HttpResponse(me.username)
        else:
            return redirect('/sign-in/')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
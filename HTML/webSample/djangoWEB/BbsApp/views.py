from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.


def loginForm(request) :
    if request.session.get('user_id'):
        context = {'id' : request.session['user_id'],
                   'name' : request.session['user_name']}
        return render(request, 'home.html', context)
    return render(request, 'login.html')

def registerForm(request) :
    return render(request, 'join.html')

def register(request):
    if request.method == 'POST':
        id   = request.POST['id']
        pwd  = request.POST['pwd']
        name = request.POST['name']
        register = BbsUserRegister(user_id=id, user_pwd=pwd, user_name=name)

        # insert into table values('')
        # model(attr = value, atrr = value .... )
        # -> model.save()

        register.save()
        return redirect('index')

def login(request):
    if request.method == 'GET':
        return redirect('login')
    elif request.method == 'POST':
        id  = request.POST['id']
        pwd = request.POST['pwd']
        # user = BbsUserRegister.objects.filter(user_id=id, user_pwd=pwd)
        # return type list. <QuerySet [<BbsUserRegister: jslim , jslim , 임정섭>]>
        user = BbsUserRegister.objects.get(user_id=id, user_pwd=pwd)
        print('user result: ' , user)
        context = {}
        if user is not None :
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            context['name'] = request.session['user_name']
            context['id'] = request.session['user_id']
            # request.session['user_name'] = user.user_name

        return render(request, 'home.html', context)


def logout(request):
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified = True

    return redirect('index')


def board(request):
    # select * from table ;
    # -> modelName.objects.all()
    boards = Bbs.objects.all()
    print('boadrs result - ' , boards)
    context = {'boards' : boards,
               'name' : request.session['user_name'],
               'id' : request.session['user_id']}
    return render(request, 'list.html', context)


def bbsRegisterForm(request):
    context = {'name': request.session['user_name'],
               'id': request.session['user_id']}
    return render(request, 'bbsRegisterForm.html', context)

def bbsRegister(request):
    if request.method == 'GET' :
        return redirect('bbs_registerForm')
    elif request.method == 'POST' :
        title   = request.POST['title']
        content = request.POST['content']
        writer  = request.POST['writer']
        register = Bbs(title=title, content=content, writer=writer)

        Bbs.save(register)
        return redirect('bbs_list')


def fetch(request, id) :
    board = Bbs.objects.get(id=id)
    board.viewcnt = board.viewcnt + 1
    board.save()
    print('user result: ' , board)
    context = {'board' : board,
               'name' : request.session['user_name'],
               'id' : request.session['user_id']}
    return render(request, 'read.html', context)


def remove(request):
    id = request.POST['id']
    board = Bbs.objects.get(id=id)
    board.delete()
    # delete * from table where id = 1
    # -> modelName.objects.get(id=1).delete()
    return redirect('bbs_list')
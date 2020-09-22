from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *

# Create your views here.



def index(request) :
    # select * from table ;
    # -> modelName.objects.all()

    # select * from table where id = 1 ;
    # -> modelName.objects.filter(id = 1);

    # select * from table where id = 1 and pwd = 1 ;
    # -> modelName.objects.filter(id = 1 , pwd = 1)

    # select * from table where id = 1 or pwd = 1 ;
    # -> model.Name.objects.filter(Q(id = 1) | Q(pwd = 1))

    # select * from table where subject like'%공지%'
    # -> model.Name.objects.filter(subject_icontains = '공지')

    # select * from table where subject like'공지%'
    # -> model.Name.objects.filter(subject_startwith = '공지')

    # select * from table where subject like'%공지'
    # -> model.Name.objects.filter(subject_endwith = '공지')

    # insert into table values('')
    # model(attr = value, atrr = value .... )
    # -> model.save()

    # delete * from table where id = 1 ;
    # -> modelName.objects.get(id=1).delete()

    # update table set attr = value where id = 1
    # obj = modelName.objects.get(id = 1)
    # obj.attr = '변경'
    # obj.save() -- commit

    lists = Question.objects.all()
    print("-"*50)
    print(lists)
    print("-"*50)
    context = {'lists' : lists}
    return render(request, 'polls/index.html', context)


def choice(request, q_id) :
    print('param q_id', str(q_id))
    lists = get_object_or_404(Question, pk=q_id)
    print("_" * 100)
    print(lists)
    print("-" * 100)
    context = {'clist' : lists}

    return render(request, 'polls/choice.html', context)


def vote(request) :
    choice = request.POST['choice']
    question_id = request.POST['question_id_choosen']
    print('param value choice - ', str(choice))
    print('param value id - ', str(question_id))

    question = get_object_or_404(Question, pk=question_id)
    checked_choice = question.choice_set.get(pk=choice)
    checked_choice.votes += 1
    checked_choice.save()

    context = {}
    request.session['question_id'] = question_id
    return redirect('result')

    # return HttpResponseRedirect(reverse('result', args=(question_id,)))
    # return render(request, 'polls/result.html', context)
    #   -> 투표 결과를 심어줄 수 없어.
    # 새 request로 redirect 해야함
    # redirect 하기 위해서는 url을 리버스 해주는 녀석이 필요
    # 화면 이동이아니라 새로운 request를 발생해서 새로운 페이지로 넘어가게 해주면되요
    # 페이지가 열릴때 request를 보내서 페이지를 가져와야 한다.
    # 특정 모델로 부터 정보를 가져와야한다. 그럴라면 단순하게 render를 통해가지고 화면을 포워드 시켜야되는게 아니라
    #


def result(request) :
        question_id = request.session['question_id']
        print('------------------ views.result', str(question_id))
        question = get_object_or_404(Question, pk=question_id)
        context = { 'question' : question}
        return render(request, 'polls/result.html', context)



from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from myinfo.models import Survey, Answer
from django.contrib.auth.hashers import make_password
import bcrypt
from user.models import UserSecondPw
from user.forms import UserSecondForm

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def index(request):
    return render(request, 'myinfo/myinfo.html')

def feedback(request):
    survey_list=Survey.objects.order_by('-survey_idx')
    context = { 'survey_list': survey_list}
    return render(request, 'myinfo/feedback.html', context)

def second_auth(request):
    if request.method=='GET':
        return render(request, 'myinfo/twoauth.html')
    elif request.method=='POST':
        password=request.POST.get('password').encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        usersecond=UserSecondPw()
        usersecond.user=request.user
        usersecond.pw=hashed_password
        usersecond.save()
        return redirect('pdfextract:index')


def get_second_pw(request):
    form = UserSecondForm()
    return render(request, 'movie_form.html', {
        'form': form,
    })
@csrf_exempt
def save_survey(request):
    dto = Answer(username=request.POST["username"],
                 survey_idx=request.POST["survey_idx"], num=request.POST["num"])
    dto.save()
    

    return redirect('myinfo:feedback')

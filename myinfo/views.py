
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from myinfo.models import Survey, Answer
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login')
def index(request):
    return render(request, 'myinfo/myinfo.html')

@login_required(login_url='/user/login')
def feedback(request):
    survey_list=Survey.objects.order_by('-survey_idx')
    context = { 'survey_list': survey_list}
    return render(request, 'myinfo/feedback.html', context)


@csrf_exempt
@login_required(login_url='/user/login')
def save_survey(request):
    dto = Answer(username=request.POST["username"],
                 survey_idx=request.POST["survey_idx"], num=request.POST["num"])
    dto.save()
    

    return redirect('myinfo:feedback')
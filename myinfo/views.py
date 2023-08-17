
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from myinfo.models import Survey, Answer


def index(request):
    return render(request, 'myinfo/myinfo.html')

def feedback(request):
    survey_list=Survey.objects.order_by('-survey_idx')
    context = { 'survey_list': survey_list}
    return render(request, 'myinfo/feedback.html', context)
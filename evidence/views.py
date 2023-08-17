from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Evidence
from .forms import EvidenceForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator  
from django.db.models import Q
from user.models import UserSecondPw
from user.forms import UserSecondForm
import bcrypt

@login_required
def write(request):

    if request.method=='GET':
        form=EvidenceForm()
        return render(request, 'evidence/evidence_form.html', {'form':form})

    elif request.method=='POST':
        form=EvidenceForm(request.POST)
        if form.is_valid():
            evidence=form.save(commit=False)
            evidence.user=request.user
            if len(request.FILES) != 0:
                evidence.attached=request.FILES["upload"]
                evidence.file_name=request.FILES["upload"].name
            evidence.crime=request.POST.get('crime')
            evidence.created_at=timezone.now()
            # evidence.crime=crime_data
            evidence.save()
            return redirect('evidence:lists')

def lists(request):
    search_kind=request.GET.get('searchKind','전체')
    print(search_kind)
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    crimes=['전체', '모욕', '명예훼손', '음란','기타']
    evidence_list = Evidence.objects.filter(user=request.user)
    if kw:
        if search_kind == '전체':
            print("전체")
            evidence_list = evidence_list.filter(
                Q(title__icontains=kw) |  
                Q(content__icontains=kw)
            ).distinct()
        else:
            print("else")
            evidence_list = evidence_list.filter(
                Q(title__icontains=kw) |  
                Q(content__icontains=kw) |  
                Q(crime__icontains=search_kind)
            ).distinct()
    elif search_kind == '전체':
        evidence_list = Evidence.objects.filter(user=request.user)
    else:
        evidence_list = evidence_list.filter( 
                    Q(crime__icontains=search_kind)
                ).distinct()

    paginator = Paginator(evidence_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'evidence_list': page_obj, 'page': page, 'kw': kw, 'select_crime':search_kind, 'crimes':crimes}
    return render(request, 'evidence/evidence_list.html', context)

def index(request):
    return render(request, 'evidence/index.html')

@login_required(login_url='/user/login')
def detail(request, pk):
    evidence=Evidence.objects.get(pk=pk)
    return render(request, 'evidence/evidence_detail.html', {'evidence':evidence})

def delete(request, pk):
    print("pk"+pk)
    if request.method == "POST":
        form = UserSecondForm(request.POST)
        if form.is_valid():
            in_pw=form.cleaned_data["pw"].encode('utf-8')
            user = UserSecondPw.objects.filter(user=request.user)
            if len(user) == 1:
                if bcrypt.checkpw(in_pw, user[0].pw):
                    print('일치함')
                else:
                    print('일치 X')


            return HttpResponse(status=204)
    else:
        form = UserSecondForm()
    return render(request, 'evidence/evidence_secondform.html', {
        'form': form,
    })



    # evidence=get_object_or_404(Evidence, pk=pk)
    # if request.user.is_authenticated:
    #     if request.user==evidence.user:
    #         user = UserSecondPw.objects.filter(user=request.user)
    #         if len(user) == 1:
    #             # bcrypt.checkpw(입력받은 비밀번호, 저장된 비밀번호)
    #             return user[0]
            
    #         evidence.delete()
    #         return redirect('evidence:lists')
    # return redirect('evidence:detail', evidence.pk)

@login_required(login_url='/user/login')
def update(request, pk):
    evidence=Evidence.objects.get(pk=pk)
    if request.method=="GET":
        evidenceForm=EvidenceForm(instance=evidence)
        context = {'form': evidenceForm}
        return render(request, 'evidence/evidence_modify.html', context)
    elif request.method=="POST":
        evidenceForm=EvidenceForm(request.POST, instance=evidence)
        if evidenceForm.is_valid():
            evidence=evidenceForm.save(commit=False)
            if len(request.FILES) != 0:
                evidence.attached=request.FILES["upload"]
            evidence.save()
        return redirect('evidence:detail', evidence.pk)

def get_second_pw(request):

    if request.method == "POST":
        form = UserSecondForm(request.POST)
        if form.is_valid():
            in_pw=form.cleaned_data["pw"].encode('utf-8')
            user = UserSecondPw.objects.filter(user=request.user)
            if len(user) == 1:
                if bcrypt.checkpw(in_pw, user[0].pw):
                    print('일치함')
                else:
                    print('일치 X')


            return HttpResponse(status=204)
    else:
        form = UserSecondForm()
    return render(request, 'evidence/evidence_secondform.html', {
        'form': form,
    })
    

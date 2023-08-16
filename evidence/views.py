from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Evidence
from .forms import EvidenceForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator  
from django.db.models import Q


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
            if request.FILES.get('file') is not None:
                evidence.attached=request.FILES["upload"]
            evidence.created_at=timezone.now()
            evidence.save()
            return redirect('evidence:lists')

def lists(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    evidence_list = Evidence.objects.order_by('-created_at')
    if kw:
        evidence_list = evidence_list.filter(
            Q(title__icontains=kw) |  
            Q(content__icontains=kw) |  
            Q(crime__icontains=kw)
        ).distinct()

    paginator = Paginator(evidence_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'evidence_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'evidence/evidence_list.html', context)

def index(request):
    return render(request, 'evidence/index.html')

@login_required(login_url='/user/login')
def detail(request, pk):
    evidence=Evidence.objects.get(pk=pk)
    return render(request, 'evidence/evidence_detail.html', {'evidence':evidence})

@require_POST
def delete(request, pk):
    evidence=get_object_or_404(Evidence, pk=pk)
    if request.user.is_authenticated:
        if request.user==evidence.user:
            evidence.delete()
            return redirect('evidence:lists')
    return redirect('evidence:detail', evidence.pk)

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
            evidence.save()
        return redirect('evidence:detail', evidence.pk)

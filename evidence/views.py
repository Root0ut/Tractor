from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Evidence
from .forms import EvidenceForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    evidence_list = Evidence.objects.order_by('-created_at')
    context = {'evidence_list': evidence_list}
    return render(request, 'evidence/evidence_list.html', context)

def index(request):
    return render(request, 'evidence/index.html')

@login_required
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

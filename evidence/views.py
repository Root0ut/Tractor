from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Evidence
from .forms import EvidenceForm

def write(request, evidence_id):
    if request.method=='GET':
        form=EvidenceForm()
        return render(request, 'evidence/evidence_form.html', {'form':form})

    elif request.method=='POST':
        form=EvidenceForm(request.POST)
        if form.is_valid():
            evidence=form.save(commit=False)
            evidence.attached=request.FILES["upload"]
            evidence.created_at=timezone.now()
            evidence.save()
            return redirect('evidence:detail', evidence_id=evidence.id)

def list(request):
    evidence_list = Evidence.objects.order_by('-created_at')
    context = {'evidence_list': evidence_list}
    return render(request, 'evidence/evidence_list.html', context)

def index(request):
    return render(request, 'evidence/index.html')

def detail(request, pk):
    evidence=Evidence.objects.get(pk=pk)
    return render(request, 'evidence/evidence_detail.html', {'evidence':evidence})
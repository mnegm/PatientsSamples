from django.shortcuts import render
from .models import Patient, Sample
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def patientView(request):
    patients = Patient.objects.all()
    context= {'patients': patients}
    return render(request, 'patient.html', context)

@login_required
def sampleView(request):
    samples= Sample.objects.all()
    context= {'samples':samples}
    return render(request,'sample.html',context)

@login_required
def refregatorView(request):
    samples=Sample.objects.order_by('refregator')
    context = {'samples': samples}
    return render(request, 'refregator.html', context)

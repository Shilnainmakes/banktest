from django.shortcuts import render,redirect, get_object_or_404
from django import forms
from .models import Form,Branch
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import RegistrationForm


# Create your views here.
def index(request):
    return render(request,'Home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'Register.html')

#def form1(request):
#    return render(request, 'form.html')

def submit(request):
    return render(request, 'submit.html')

def person_create_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_page')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Form, pk=pk)
    form = RegistrationForm(instance=person)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request,'branches_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)









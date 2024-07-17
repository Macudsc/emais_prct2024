from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm

def patient_page(request):
    return render(request, 'patient/patient.html')

def register(request):
  if request.method == 'POST':
    form=NewUserForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request, user)
      return redirect('core:index')
  form=NewUserForm()
  context={'form':form}
  return render(request, 'patient/register.html', context)

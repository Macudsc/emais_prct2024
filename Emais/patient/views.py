from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

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

#profile
@login_required # расширение, чтобы нельзя было зайти на страницу без входа в УЗ
def patient_myinfo(request):
    return render(request, 'patient/myinfo.html')
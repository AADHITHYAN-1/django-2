from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,"home.html",{})




def authview(request):
    if request.method=='post':
        form=UserCreationForm(request.post or None)
        if form.is_valid():
            form.save()
        else:
            return None
    form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required
def home(request):
    return render(request, "home.html", {})

def authview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

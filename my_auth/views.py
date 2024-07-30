from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'auth/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Automatically log in user after registration
            return redirect('home')  # Redirect to the home page
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})
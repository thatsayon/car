from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from cars.models import Car
from . import forms 

def Login(request):
    return render(request, 'auth.html')

def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect("Home")
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'auth.html', {'form': register_form, 'type': 'Register'})
    

class UserLoginView(LoginView):
    template_name = 'auth.html'

    def get_success_url(self):
        return reverse_lazy("Home")
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "Logged in failed")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context 

def profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('Profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    
    cars = request.COOKIES.get('car')
    cars = cars.split(" ")
    car = []
    for data in cars:
        car.append(Car.objects.filter(pk=data))

    return render(request, 'profile.html', {'form': profile_form, 'type': 'Profile', 'cars': car})

def user_logout(request):
    logout(request)
    return redirect('Home')

from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from . import models
from . import forms

def carinfo(request, id):
    car = models.Car.objects.get(pk=id)
    return render(request, 'carinfo.html', context={'car': car})

class CarInfoView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'carinfo.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car 
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()

        comment_form = forms.CommentForm()
        context['comment'] = comments 
        context['comment_form'] = comment_form
        return context 

def buycar(request, id):
    response = HttpResponseRedirect('/')  
    # car = models.Car.objects.get(pk=id)
    # car.quantity = car.quantity - 1
    # car.save()
    car_id = request.COOKIES.get('car')
    car_id += " "
    car_id += str(id)
    response.set_cookie('car', car_id)
    return response
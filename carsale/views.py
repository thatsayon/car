from django.shortcuts import render
from cars import models

def home(request, cat_slug=None):
    cars = models.Car.objects.all()
    if cat_slug is not None:
        brand = models.Brand.objects.get(slug=cat_slug)
        cars = models.Car.objects.filter(brand_name=brand)
    brands = models.Brand.objects.all()
    data = {
        "brands": brands,
        "cars": cars
    }
    return render(request, "home.html", context=data)
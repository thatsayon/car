from django.urls import path 
from . import views

urlpatterns = [
    # path('car/<int:id>/', views.carinfo, name="Carinfo"),
    path('car/<int:id>/', views.CarInfoView.as_view(), name="Carinfo"),
    path('bcar/<int:id>/', views.buycar, name="Buy"),
]

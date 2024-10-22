from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', views.calculator),
    path('', views.calculator, name='home'),
    path('evenodd/', views.evenodd),
]

from . import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    path('', views.home, name='home'),
    path('patient/', views.patientView, name='patientPage'),
    path('samples/', views.sampleView, name='samplePage'),
    path('refregator/', views.refregatorView, name='refregatorPage')

]
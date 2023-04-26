from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor,  name='doctor')

]
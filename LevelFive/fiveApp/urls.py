
from django.urls import path
from fiveApp import views

# TEMPLATE URLs
app_name = 'fiveApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]

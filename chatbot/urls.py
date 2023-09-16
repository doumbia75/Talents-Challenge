from django.shortcuts import redirect
from django.urls import path

from chatbot.views import register, logins, chatbots, index, logouts

urlpatterns = [

    path('', index, name='index'),
    path('register/', register, name="register"),
    path('login/', logins, name="login"),
    path('chatbot', chatbots, name='chatbots'),
    path('logout/', logouts, name="logout"),
]
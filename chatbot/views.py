from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
import os
import openai
import openai


from chatbot.models import Compte, Message
from env import Openai_Keys, Openai_Keys1


# def streamlit_view(request):
#      return render(request, 'streamlit_template.html')
def index(request):

    return render(request, 'chatbot/index.html')

def chatbots(request):
    if request.user.is_authenticated:
        hist = Message.objects.filter(user_id=request.user.id)[:8]
        if request.method == "POST":
            message = request.POST.get("messages")
            openai.api_key = Openai_Keys1
            if openai.api_key:



                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-16k",
                    messages=[
                        {"role": "system", "content": message},

                    ]
                )
                reponse = completion.choices[0].message.content
                gestionMessage(message,reponse, request.user.id)





            return redirect('chatbots')

        if hist:
            recente = Message.objects.filter(user_id=request.user.id).latest( 'create_date')
            context = {
                "hists": hist,
                "recente": recente,

            }
        else:
            context = {

            }

    else:
        return redirect('login')
    return render(request, "chatbot/chatbots.html", context=context)

def gestionMessage(message,reponse,user):
    chat = Message(message=message, reponse=reponse, user_id=user)

    if chat:
        chat.save()

    return chat

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        jetons = str(uuid.uuid4())


        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password)
        if user:
            user.save()
            comptes = Compte(jetons=jetons, user_id=user.id)
            comptes.save()
            return redirect('login')
        else:
            return redirect('register')
    return render(request, "chatbot/register.html")
def logins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('chatbots')

    return render(request, "chatbot/login.html")


def logouts(request):
    if request.user.is_authenticated:
        # for sesskey in request.session.keys():
        #     del request.session[sesskey]
        logout(request)
        return redirect('index')
    return HttpResponse("vous n'etes pas connectes")
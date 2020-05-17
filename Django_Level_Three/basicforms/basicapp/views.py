from django.shortcuts import render
from .forms import Userform, Userprofileinfoforms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
from . import forms

def index(request):

    return render(request, 'basicapp/index.html')

@login_required
def special(request):
    return HttpResponse(" YOU ARE LOGGED IN, NICE!")


@login_required    
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method =='post':
        user_form = Userform(data=request.post)
        profile_form = Userprofileinfoforms(data = request.post)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = Userform()
        profile_form = Userprofileinfoforms()

    return render(request,'basicapp/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered': registered})

def user_login(request):

    if request.method =='post':
        username = request.post.get('username')
        password = request.post.get('password')


        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print("USERNAME:{} AND PASSWORD{}".format(useranme,password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")

    else:
        return render(request,'basicapp/login.html',{})

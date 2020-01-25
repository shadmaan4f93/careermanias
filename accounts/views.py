import json
import os
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from careermania import settings
from django.core.mail import EmailMessage

#-------------------------------------------------------------------------------------------

def logins(request):
    if request.is_ajax():
        mimetype = 'application/json'
        success = False
        message = None
        try:   
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                success = True
                message = "Login Success"
            else:
                success = False
                message = "Invalid User!"        
        except:
            success = False
            message = "Invalid User!"    
        return HttpResponse(json.dumps({"success": success, "message": message}), mimetype) 
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    mimetype = 'application/json'
    success = False
    errors = None
    message = None

    if request.is_ajax():
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your skwebinfo account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': user.pk,
                'token':account_activation_token.make_token(user),
            })
            from_email = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            msg = EmailMessage(subject, message, from_email, [to_email])
            msg.content_subtype = "html"
            res = msg.send()
            if(res == 1):
                success = True
                message = "Please open your email and confirm account to login!" 
            else:
                success = True
                message = "Account created successfully. Contact admin to activate!"                     
        else:
            errors = form.errors.as_json()
            success = False
            message = "Invalid data passed!"
        return HttpResponse(json.dumps({"success": success, "message": message, "errors": errors}), mimetype)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#---------------------------------------------------------------------------------------------

def activate(request, uidb64, token):
    uid = uidb64
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        profile = Profile(user=user)
        profile.save()
        login(request, user)
        messages.add_message(request, messages.INFO, 'Thank you for your email confirmation.')
        return redirect('/blogs')
    else:
        return HttpResponse('Activation link is invalid!')
#---------------------------------------------------------------------------------------------
@login_required
def edit_profile(request):
    try:
        if request.method == 'POST':    
            form = ProfileUpdateForm(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                return redirect('/accounts/user/profile')
        else:
            form = ProfileUpdateForm(instance = request.user)
    except:
        form = ProfileUpdateForm(instance = request.user)
    return render(request, 'accounts/edit_profile.html', {'form':form})

#---------------------------------------------------------------------------------------------
@login_required
def add_user_info(request):
    if request.method == 'POST':    
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            messages.add_message(request, messages.INFO, 'Congratulations yor information has been added to your profile')
            return redirect('/accounts/user/profile/')
        else:
            messages.add_message(request, messages.INFO, 'Something wrong')
            return redirect('/accounts/user/profile/add/')
    else:
        form = UserInfoForm()
       
    return render(request, 'accounts/user_info_update.html', {'form':form})


#--------------------------------------------------------------------------------------------
@login_required
def profile(request):
    profile = {}
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        pass  
    return render(request, 'accounts/profile.html', {"profile":profile })

#-----------------------------------------------------------------------------------------------
@login_required
def change_password(request):
    try:
        if request.method == 'POST':    
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('/accounts/user/profile/')
        else:
            form = PasswordChangeForm(user=request.user)
    except:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def signup_success(request):
    cotext = {
        "message": "Registration Success!"
    }
    return render(request, 'accounts/signup_success.html', cotext)




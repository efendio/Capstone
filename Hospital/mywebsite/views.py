from django.shortcuts import render 

import random
import smtplib
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

def otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not email:
            return JsonResponse({"status": "error", "message": "Email is required"}, status=400)

        otp = random.randint(100000, 999999)
        request.session["otp"] = otp  

        subject = "Your OTP Code"
        message = f"Your OTP code is {otp}. It is valid for 5 minutes."
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, sender_email, recipient_list)
            return JsonResponse({"status": "success", "message": "OTP sent successfully!"})
        except smtplib.SMTPException as e:
            return JsonResponse({"status": "error", "message": f"Failed to send email: {str(e)}"}, status=500)


def index(request):
    context = {
        'title' : 'Health Care Services',
        'heading' : 'AI-HealthCare',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail.com',
        'address' : 'Bebora, Dili, Timor-Leste',
       
    }
    return render(request, 'index.html', context) 

def index2(request):
    context = {
        'title' : 'Health Care Services',
        'heading' : 'AI-HealthCare',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail.com',
        'address' : 'Bebora, Dili, Timor-Leste',
        
    }
    return render(request, 'index2.html', context)

def login(request):
    context = {
        'title' : 'Login',
        'heading' : 'Login',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail.com',
        'address' : 'Bebora, Dili, Timor-Leste',
        
    }
    return render(request, 'login.html', context)

def registration(request):
    context = {
        'title' : 'Registration',
        'heading' : 'Registration',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail',
        'address' : 'Bebora, Dili, Timor-Leste',
    }
    return render(request, 'registration.html', context)

def profile(request):
    context = {
        'title' : 'Profile',
        'heading' : 'Profile',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail',
        'address' : 'Bebora, Dili, Timor-Leste',
    }
    return render(request, 'profile.html', context)

def about(request):
    context = {
        'title' : 'About',
        'heading' : 'About',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail',
        'address' : 'Bebora, Dili, Timor-Leste',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title' : 'Contact',
        'heading' : 'Contact',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail',
        'address' : 'Bebora, Dili, Timor-Leste',
    }
    return render(request, 'about.html', context)

def forgot(request):
    context = {
        'title' : 'Forgot Password',
        'heading' : 'Forgot Password',
        'number' : '+670 7498 2319',
        'email' : 'HealthCare@gmail',
        'address' : 'Bebora, Dili, Timor-Leste',
    }
    return render(request, 'forgot.html', context)

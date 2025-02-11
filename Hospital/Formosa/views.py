from django.shortcuts import render


def index(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/index.html', context)

def about(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/about.html', context)

def appointment(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/appointment.html', context)

def contact(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/contact.html', context)

def feature(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/feature.html', context)

def service(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00 PM',
    }
    return render(request, 'Formosa/service.html', context)

def team(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00',
    }
    return render(request, 'Formosa/team.html', context)

def testimonial(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00',
    }
    return render(request, 'Formosa/testimonial.html', context)

def blank(request):
    context = {
        'title': 'Formosa',
        'heading': 'Formosa',
        'number' : '+670 7498 2319',
        'email' : 'Formosa@gmail.com',
        'address' : 'Audian, Dili, Timor-Leste',
        'time' : 'Mon - Fri : 09.00 AM - 09.00',
    }
    return render(request, 'Formosa/blank.html', context)



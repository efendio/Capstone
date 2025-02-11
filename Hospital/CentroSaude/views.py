from django.shortcuts import render

def index(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaude@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/index.html', context)

def about(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/about.html', context)

def appointment(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/appointment.html', context)

def blog(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/blog.html', context)

def contact(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/contact.html', context)

def detail(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/detail.html', context)

def price(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/price.html', context)

def search(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/search.html', context)

def service(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/service.html', context)

def team(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/team.html', context)

def testimonial(request):
    context = {
        'title': 'Centro Saude Comoro',
        'heading': 'Centro Saude Comoro',
        'number' : '+670 7467 9823',
        'email' : 'CentroSaudeComoro@gmail.com', 
        'address' : 'Comoro, Dili, Timor-Leste',
    }
    return render(request, 'CentroSaude/testimonial.html', context)

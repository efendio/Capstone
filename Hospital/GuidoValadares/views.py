from django.shortcuts import render


def index(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/index.html', context)

def about(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '+670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/about.html', context)

def details(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '+670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/blog-details.html', context)

def blog(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '+670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/blog.html', context)

def contact(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '+670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/contact.html', context)

def doctors(request):
    context = {
        'title': 'Hospital Nacional Guido Valadares',
        'heading': 'Hospital Nacional Guido Valadares',
        'number' : '+670 7498 2319',
        'email' : 'GuidoValadares@gmail.com',
        'address' : 'Bidau, Dili, Timor-Leste',
    }
    return render(request, 'GuidoValadares/doctors.html', context)



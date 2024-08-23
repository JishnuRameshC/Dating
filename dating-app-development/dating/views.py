from django.shortcuts import render


# Create your views here.

def TestView(request):
    return render(request, 'index.html')

def  sent(request):
    return render(request, 'sent.html')

def accept(request):
    return render(request, 'accept.html')


def messgage(request):
    return render(request, 'message.html')

def contact(request):
    return render(request, 'contacted.html')

def shortlist(request):
    return render(request, 'shortlist.html')

def shortlist_by(request):
    return render(request, 'shortlist_by.html')


def received(request):
    return render(request, 'received.html')

def reject(request):
    return render(request, 'reject.html')

def viewed_myprofile(request):
    return render(request, 'viewed_myprofile.html')


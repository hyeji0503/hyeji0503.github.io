from django.shortcuts import render, redirect

def first(request):
    return render(request, 'first.html')
    

def second(request):
    return render(request, 'second.html')
    
    
def third(request):
    return render(request, 'third.html')


def firth(request):
    if request.method == "POST":
        name = request.POST.get('name')
        redirect('firth')
    return render(request, 'firth.html', {'name': name})
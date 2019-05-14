from django.shortcuts import render

def main(request):
    return render(request, 'main.html')
    

def holy(request):
    return render(request, 'holy.html')
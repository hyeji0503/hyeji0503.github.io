from django.shortcuts import render, redirect

def order(request):
    return render(request, 'order.html')


def exit(request):
    return render(request, 'exit.html')
    

def get_name(request):
    if request.method == "POST":
        name = request.POST.get('name')
        redirect('get_name')
    return render(request, 'get_name.html', {'name': name})
    
    
def order_complete(request):
    return render(request, 'order_complete.html')
    

def order_side(request):
    return render(request, 'order_side.html')
    
def order_side_only(request):
    return render(request, 'order_side_only.html')
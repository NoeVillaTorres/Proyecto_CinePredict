from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def predicciones_page(request):
    return render(request, 'basic.html')


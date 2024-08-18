from django.shortcuts import render

# Create your views here.
#Quando for criar uma página. Seguri o padrão: url --> view --> template

def homepage(request):
    return render(request, 'homepage.html')
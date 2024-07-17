from django.shortcuts import render

def bare(request):
    return render(request, 'Emais/bare.html')
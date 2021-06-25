from django.shortcuts import render

# Create your views here.

def hi_universe(request):
    return render(request, "hi_universe.html", {})

from django.shortcuts import render

# Create your views here.

def dictionary_view(request):
    return render(request, 'dictionary.html')
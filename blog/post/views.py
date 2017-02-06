from django.shortcuts import render

# Create your views here.

def list(request):

    context = {
        "title" : "List"
    }

    return render(request, "index.html", context)
from django.shortcuts import render


# Create your views here.

def work(request):
    context = {

    }
    return render(request, 'pages/work.html', context)

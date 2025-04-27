from django.shortcuts import render


def ping_view(request):
    return render(request, 'ping_app/ping.html')


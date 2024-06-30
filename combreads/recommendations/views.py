from django.shortcuts import render


def suggestions(request):
    return render(request, 'recommendations/recopage.html')
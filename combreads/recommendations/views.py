from django.shortcuts import render
from .models import DailyReco
from django.utils import timezone

def suggestions(request):
    today = timezone.now().date()
    daily_reco = DailyReco.objects.filter(date=today).first()
    return render(request, 'recommendations/recopage.html', {'daily_reco': daily_reco})
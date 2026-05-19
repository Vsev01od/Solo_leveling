from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta
from django.utils import timezone

def main(request):
    if request.method == "POST":
        yesterday = timezone.now().date() - timedelta(days=1)
        if request.user.profile.fire_mode_bool == timezone.now().date():
            return redirect("/")
        if request.user.profile.fire_mode_bool != yesterday:
            request.user.profile.fire_mode = 0
        request.user.profile.fire_mode += 1
        request.user.profile.fire_mode_bool = timezone.now().date() 
        request.user.profile.save()
        return redirect("/")


    template = "homepage/homepage.html"
    fire = request.user.profile.fire_mode
    context = {
        "fire": fire,
    }
    return render(request, template, context)
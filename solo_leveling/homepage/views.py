# views.py
from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta
from django.utils import timezone
import random

def fire_day_word(count):
    if 11 <= count % 100 <= 14:
        return "дней"
    last_digit = count % 10
    if last_digit == 1:
        return "день"
    elif 2 <= last_digit <= 4:
        return "дня"
    else:
        return "дней"

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
        videos = ["1.mp4", "2.mp4", "3.mp4", "4.mp4",
                  "5.mp4", "6.mp4", "7.mp4", "8.mp4",
                  "9.mp4", "10.mp4", "11.mp4", "12.mp4",
                  "13.mp4", "14.mp4", "15.mp4", "16.mp4",
                  "17.mp4", "18.mp4", "19.mp4",
        ]
        random_video = random.choice(videos)
        request.session['fire_video'] = f"/static/videos/{random_video}"
        return redirect("/")

    fire_video = request.session.pop('fire_video', None)
    
    template = "homepage/homepage.html"
    fire = request.user.profile.fire_mode
    context = {
        "fire": fire,
        "fire_day_word": fire_day_word(fire),
        "fire_video": fire_video,
    }
    return render(request, template, context)
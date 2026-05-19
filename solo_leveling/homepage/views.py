from django.shortcuts import render, redirect

def main(request):
    if request.method == "POST":
        request.user.profile.fire_mode += 1
        request.user.profile.save()
        return redirect("/")


    template = "homepage/homepage.html"
    fire = request.user.profile.fire_mode
    context = {
        "fire": fire,
    }
    return render(request, template, context)
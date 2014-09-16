from django.shortcuts import render

from forms import FragForm


def home(request):

    if "url" in request.GET:
        form = FragForm(request.GET)
        if form.is_valid():
            from django.http import HttpResponse
            return HttpResponse("soup it")
    else:
        form = FragForm()

    return render(request, "home.html", {
        "form": form,
    })

from django.shortcuts import redirect, render
from .models import Contact


def home_view(request):
    template_name = "portfolio/home.html"

    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"))
        request.session["show_popup"] = True
        return redirect("home_view_urls")

    show_popup = request.session.pop("show_popup",False)
    return render(request,template_name,{"show_popup": show_popup})
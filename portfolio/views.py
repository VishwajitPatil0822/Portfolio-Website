from django.shortcuts import render

def home_view(request):
    template_name = 'portfolio/home.html'
    context = {}
    return render(request, template_name, context)
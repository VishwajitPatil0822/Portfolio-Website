from django.shortcuts import render,redirect
from .models import Contact

def home_view(request):
    template_name = 'portfolio/home.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        request.session['show_popup'] = True
        return redirect('home_view_urls')

    show_popup = request.session.pop('show_popup', False)
    context = {'show_popup': show_popup}
    return render(request, template_name, context)
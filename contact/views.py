from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, "MainPage/index.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'nume': form.cleaned_data['nume'],
                'prenume': form.cleaned_data['prenume'],
                'email': form.cleaned_data['email'],
                'subiect': form.cleaned_data['subiect'],
                'mesaj': form.cleaned_data['mesaj'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("index")

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})


# urlpatterns = [
#     path("", views.homepage, name="homepage"),
#     path("contact", views.contact, name="contact"),
#
# ]
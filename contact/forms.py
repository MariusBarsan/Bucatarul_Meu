from django import forms


class ContactForm(forms.Form):
    nume = forms.CharField(max_length=100, label='Va rog introduceti numele :')
    prenume = forms.CharField(max_length=100, label='Va rog introduceti prenumele :')
    email = forms.EmailField(required=False, label='Va rog introduceti adresa de E-Mail :')
    subiect = forms.CharField(max_length=100)
    mesaj = forms.CharField(widget=forms.Textarea)





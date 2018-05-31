from django import forms
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def send_email(self):
        body = '<br />'.join(['Nome:', self.cleaned_data['name'], '',
                              'E-mail', self.cleaned_data['email'], '',
                              'Mensaxe:', self.cleaned_data['message']])

        email = EmailMultiAlternatives(
            subject=self.cleaned_data['subject'],
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.ADMINS,
            reply_to=[self.cleaned_data['email']],
        )
        email.attach_alternative(body, 'text/html')

        email.send()

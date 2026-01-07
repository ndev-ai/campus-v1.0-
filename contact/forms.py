from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form for user submissions"""

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Your Name'),
                'class': 'contact-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+998 90 123-45-67',
                'class': 'contact-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': _('What is this about?'),
                'class': 'contact-input',
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': _('Your message...'),
                'class': 'contact-input',
            }),
        }
        labels = {
            'name': _('Name'),
            'phone': _('Phone Number'),
            'subject': _('Subject'),
            'message': _('Message'),
        }

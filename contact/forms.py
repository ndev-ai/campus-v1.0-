from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form for user submissions"""

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'style': 'width: 100%; padding: 12px 16px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(132, 204, 22, 0.2); border-radius: 8px; color: white; font-size: 14px; outline: none; transition: all 0.3s;'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'style': 'width: 100%; padding: 12px 16px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(132, 204, 22, 0.2); border-radius: 8px; color: white; font-size: 14px; outline: none; transition: all 0.3s;'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'What is this about?',
                'style': 'width: 100%; padding: 12px 16px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(132, 204, 22, 0.2); border-radius: 8px; color: white; font-size: 14px; outline: none; transition: all 0.3s;'
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Your message...',
                'style': 'width: 100%; padding: 12px 16px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(132, 204, 22, 0.2); border-radius: 8px; color: white; font-size: 14px; outline: none; resize: vertical; transition: all 0.3s;'
            }),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

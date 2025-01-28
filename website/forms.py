from django import forms 
from website import models
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Contact
        fields = '__all__'


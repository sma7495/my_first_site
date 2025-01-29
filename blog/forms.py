from django import forms 
from blog import models
from captcha.fields import CaptchaField


class CommentsForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Comments
        exclude = ["reply", "approved", "updated_date", "created_date"]

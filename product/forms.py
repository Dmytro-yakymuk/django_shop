from django import forms

from .models import Reviews

class ReviewForm(forms.ModelForm):
    """ Форма отзивів """

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
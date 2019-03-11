from django import forms
from .models import *


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Progress
        fields = ('word_id',)


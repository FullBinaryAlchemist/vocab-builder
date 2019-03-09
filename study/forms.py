from django import forms
from .models import *


"""class ListDetail(forms.ModelForm):
    categories = forms.List.objects.all()

    class Meta:
        model = List
        fields = ('categories',)


class WordsDetail(forms.ModelForm):
    tot_words = {}
    tot_gre_words = WordList.objects.filter(word_id__contains='GRE')
    tot_sat_words = WordList.objects.filter(word_id__contains='SAT')
    tot_words = {'gre': tot_gre_words, 'sat': tot_sat_words, }

    class Meta:
        model = WordList
        fields = ('',)

class ReviewDetail(forms)"""
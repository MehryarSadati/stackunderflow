from django import forms

from .models import *


class QuestionForm(forms.ModelForm):
    pass


class AnswerForm(forms.ModelForm):
    pass


class SearchForm(forms.Form):
    pass


class TagForm(forms.ModelForm):
    pass

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget = forms.NumberInput(attrs={
            'min': 1, 'max': 5, 'step': 1, 'placeholder': '1-5',
        })
        self.fields['rating'].label = "Rating (1-5)"

from django import forms
from .models import myapp_db
import datetime


class myapp_form(forms.ModelForm):
    class Meta:
        model = myapp_db
        fields = ['topics', 'notes', 'date', 'time']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
    def clean_date(self):
        date = self.cleaned_data['date']
        today = datetime.date.today()
        if date < today:
            raise forms.ValidationError("The date cannot be in the past.")
        return date



from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'dob': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            )
        }

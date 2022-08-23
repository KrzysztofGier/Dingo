from django import forms
from maths.models import Result
from maths.models import OPERATION_CHOICES

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get("value")
        error = cleaned_data.get("error")

        if value and error:
            raise forms.ValidationError("Podaj tylko jedną z wartości!")
        elif not (value or error):
            raise forms.ValidationError("Nie podano żadnej wartości!")

class OperationForm(forms.Form):
    operation = forms.ChoiceField(choices=OPERATION_CHOICES)
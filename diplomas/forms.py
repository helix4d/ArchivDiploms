from django import forms
from .models import Diploma


class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ["full_name", "issue_date", "diploma_number", "diploma_file"]

    def clean_diploma_file(self):
        file = self.cleaned_data.get("diploma_file")
        if file:
            if file.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File too large (max 5MB)")
            if not file.name.lower().endswith((".pdf", ".png")):
                raise forms.ValidationError("Only PDF and PNG allowed")
        return file

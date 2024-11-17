from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')

    # You can add custom validation if needed
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain alphabets.")
        return name

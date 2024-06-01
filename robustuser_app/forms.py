from django import forms
from .models import Bio, Certificates, Projects

class bioForm(forms.ModelForm):

    class Meta:
        model=Bio
        fields='__all__'
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'maxlength': '250',
                'required': True,
                'autofocus': True,
                'style':'width:400px;'
            }),
            'Date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date',
                'min': '1900-01-01',
                'max': '2100-12-31',
                'style': 'width:400px;'

            }),
            'Address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'maxlength': '500',
                'style': 'width:400px;'

            }),
            'Phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'maxlength': '11',
                'pattern': '[0-9]{11}',
                'title': 'Enter an 11-digit phone number',
                'style': 'width:400px;'

            }),
            'Age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age',
                'min': '0',
                'max': '150',
                'style': 'width:400px;'

            }),
            'Degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your degree',
                'maxlength': '450',
                'style': 'width:400px;'

            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'style': 'width:400px;'

            }),
            'Skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your skills',
                'maxlength': '500',
                'style': 'width:400px;'

            }),
            'Freelance': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width:30px; height:20px;'

            }),
            'Image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'width:400px;'

            }),
        }


class certificatesForm(forms.ModelForm):

    class Meta:
        model=Certificates
        fields='__all__'
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter certificate name',
                'maxlength': '250',
                'required': True,
                'autofocus': True,
                'style':'width:400px;'
            }),
            'Description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'About certificate',
                'maxlength': '250',
                'required': True,
                'autofocus': True,
                'style': 'width:400px;'
            }),
            'Image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'width:400px;'

            }),
        }

class projectsForm(forms.ModelForm):

    class Meta:
        model=Projects
        fields='__all__'
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project name',
                'maxlength': '250',
                'required': True,
                'autofocus': True,
                'style':'width:400px;'
            }),
            'Description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'About project',
                'maxlength': '250',
                'required': True,
                'autofocus': True,
                'style': 'width:400px;'
            }),
            'Image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'width:400px;'

            }),
        }
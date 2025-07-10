from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your first name',
            }
        ),
        label='1st Name',
        help_text='Write the first name here',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-a class-b',
        #     'placeholder': 'Write your first name',
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

        # widgets = {
        #     'firt_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Write your first name',

        #         }
        #     ),

        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'First name and last name cannot be the same.',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Invalid first name.',
                    code='invalid'
                )
            )

        return first_name

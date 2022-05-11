from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name' , 'contact_number']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', id: "city", 'placeholder': "Имя"}),
            'contact_number': TextInput(attrs={'data-mask': "000-000-0000"})
        }

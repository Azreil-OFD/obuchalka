from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name' , 'contact_number']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', id: "city", 'placeholder': "Введите город"})
        }

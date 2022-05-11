from django.shortcuts import render
import requests as re
from .models import User
from .forms import UserForm as CityForm



def index(request):

    if request.method == 'POST':
        if request.POST['send'] == "Отслеживать":
            form = CityForm(request.POST)
            form.save()

    form = CityForm()

    contex = {
        'form': form,
    }
    return render(request, 'stydent/index.html', contex)

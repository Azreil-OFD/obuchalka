from django.shortcuts import render
import requests as re
from .models import City
from .forms import CityForm


def recompo(citys):
    names = []
    objects = []
    for i in citys.objects.all():
        if i.name not in names:
            names.append(i.name)
            objects.append(i)
    return objects


def index(request):
    if request.method == 'POST':
        if request.POST['send'] == "Отслеживать":
            form = CityForm(request.POST)
            form.save()
        elif request.POST['send'] == "Очистить":
            City.objects.all().delete()

    cities = recompo(City)

    cities_info = []
    lang = 'ru'
    api_key = '227b04948e29055d6a4ee1aa90e7c5a9'
    img_url = "https://million-wallpapers.ru/wallpapers/6/23/337865106824502/krasivoe-svetloe-nebo-pokrytoe-oblakami.jpg"

    form = CityForm()

    for city in cities:
        url = f'''https://api.openweathermap.org/data/2.5/weather?q={city}&units=Metric&lang={lang}&appid={api_key}'''
        res = re.get(url).json()
        print(res)
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'weather': res['weather'][0]['main'],
            'icon': res['weather'][0]['icon'],
            'visibility': res['visibility'],
            'wind': res['wind']['speed'],
        }
        if city == cities[0]:
            if (city_info['weather'] == 'Clear'):
                pass
            elif(city_info['weather'] == 'Clouds'):
                img_url = 'https://cdn.profile.ru/wp-content/uploads/2021/06/7432391.jpg'

        cities_info.append(city_info)

    contex = {
        'all_info': cities_info,
        'form': form,
        'url': img_url
    }
    return render(request, 'weather/index.html', contex)

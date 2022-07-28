from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.


def my_first_url(request):
    return HttpResponse('Hello World')


def first_render(request):
    return render(request, 'index.html')


def show_words(request):
    words = ["Оті дурні, що кричать 'націоналіст!', не розуміють і ніколи не зрозуміють, "
             "що я зумів об'єднати любов до мого народу з любов'ю до всіх народів світу!",
             'Тобі, Україно моя, і перший мій подих, і подих останній тобі.',
             'Мій рідний край такий веселий,\nМій рідний край такий сумний!']
    return HttpResponse(words[randint(0, len(words))])


def first_context(request):
    words = ["Оті дурні, що кричать 'націоналіст!', не розуміють і ніколи не зрозуміють, "
             "що я зумів об'єднати любов до мого народу з любов'ю до всіх народів світу!",
             'Тобі, Україно моя, і перший мій подих, і подих останній тобі.',
             'Мій рідний край такий веселий,\nМій рідний край такий сумний!']
    return render(request, 'index_2.html', context={'Text': words[randint(0, len(words)-1)]})


def hello_name(request, name):
    return HttpResponse(f'Hello {name}')


def star_wars_home(request):
    return render(request, 'star_wars_home.html')


def star_wars_page(request, name):
    names = {
        "luck": "Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера",
        "leya": "Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.",
        "hun": "Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым пилотом является вуки по имени Чубакка."
        }
    return render(request, 'star_wars_page.html', context={'Text': names[name]})

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home_page.html')


def news(request):
    return render(request, 'news_page.html')


def head(request):
    return render(request, 'head.html')


def facts(request):
    return render(request, 'facts.html')


def contacts(request):
    return render(request, 'Contacts.html')


def history(request):
    text = """Заселення території сучасної Сумщини розпочалося приблизно 15 тис. років тому. В V-III тис. до н. е. 
    територія області була заселена ураломовними мисливсько-рибальськими племенами. Сумщина належала до ареалу 
    гребінцевої кераміки (стоянки Погорілівка, Мис Очкинський та інші). Спосіб життя культур кам'яного віку в 
    основному ґрунтувався на полюванні та рибальстві. З кінця ІІІ початку І тис. до н. е. на території Сумщини 
    жили землеробсько-скотарські племена. На берегах Сейму, Сули, Ворскли та Псла виявлено понад 70 городищ, 
    поселень та курганних могильників"""
    return render(request, 'history.html', context={'Text': text})


def history_extra(request, page):
    link = 'http://2.bp.blogspot.com/-qa9mBSlNIjo/VVI_WqQZZFI/AAAAAAAAABw/x-ob0H-6AOU/s1600/4191_html_3adff5da.png'
    url_list = {
        'people': link,
        'photos': 'https://cukr.city/wp-content/uploads/2021/09/Lenyna-Sobornaia-60-e_1.jpg'}
    text_list = {'people': 'Видатні люди Сумщини', 'photos': 'Історичні фотографії Сум'}
    return render(request, 'history.html', context={'Text': text_list[page],
                                                    'url': url_list[page]})

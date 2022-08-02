from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def current_time(request):
    now = datetime.now()
    # return HttpResponse(f'{now.strftime("%H:%M")}')
    return render(request, 'current_time.html', context={'Text': now.strftime('%H:%M'),
                                                         'Text2': now.strftime('%d.%m.%Y')})


def multiplication(request):
    result = dict()

    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(f'{i}*{j}={i * j}')
        result[f'Text{i}'] = '\t\t'.join(row)

    return render(request, 'multiplication.html', context=result)


def date_of_day(request):
    return HttpResponse(f"Цього року день програміста святкують: "
                        f"{(datetime(2022, 1, 1) + timedelta(days=265)).strftime('%d %B')}")

from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def hello(request):
    words = f'<h1>Изучаем django</h1><strong>Автор</strong>: <i>Михайлов А. Н.</i>'
    return HttpResponse(words)


def about(request):
    user_name = 'Антон'
    user_surname = 'Михайлов'
    user_dadname = 'Николаевич'
    phone_number = '8-902-171-01-01'
    email = 'inion13@gmail.com'
    lister = (f'<strong>Имя</strong>: <i>{user_name}</i><br>'
              f'<strong>Отчество</strong>: <i>{user_dadname}</i><br>'
              f'<strong>Фамилия</strong>: <i>{user_surname}</i><br>'
              f'<strong>телефон</strong>: <i>{phone_number}</i><br>'
              f'<strong>email</strong>: <i>{email}</i><br>')
    return HttpResponse(lister)


def item(request):
    global items
    for i in range(len(items)):
        if items[i]['id'] == 1:
            x = (f'<strong>Название</strong>: <i>{items[i]["name"]}</i><br>'
                 f'<strong>Количество</strong>: <i>{items[i]["quantity"]}</i><br>')
            return HttpResponse(x)
        elif items[i]['id'] == 2:
            x = (f'<strong>Название</strong>: <i>{items[i]["name"]}</i><br>'
                 f'<strong>Количество</strong>: <i>{items[i]["quantity"]}</i><br>')
            return HttpResponse(x)
        elif items[i]['id'] == 5:
            x = (f'<strong>Название</strong>: <i>{items[i]["name"]}</i><br>'
                 f'<strong>Количество</strong>: <i>{items[i]["quantity"]}</i><br>')
            return HttpResponse(x)
        if items[i]['id'] == 7:
            x = (f'<strong>Название</strong>: <i>{items[i]["name"]}</i><br>'
                 f'<strong>Количество</strong>: <i>{items[i]["quantity"]}</i><br>')
            return HttpResponse(x)
        if items[i]['id'] == 8:
            x = (f'<strong>Название</strong>: <i>{items[i]["name"]}</i><br>'
                 f'<strong>Количество</strong>: <i>{items[i]["quantity"]}</i><br>')
            return HttpResponse(x)
        else:
            return HttpResponse('error')
    items_list = f'<h1>Изучаем django</h1><strong>Автор</strong>: <i>Михайлов А. Н.</i>'
    return HttpResponse

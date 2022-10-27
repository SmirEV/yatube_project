from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    context = {
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_list(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, gr):
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)

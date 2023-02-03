from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>hello is Docker</h1>')


def second_page(request):
    return HttpResponse('А это вторая страница!')

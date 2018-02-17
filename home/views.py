from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home_page(request):
    return render(request, 'index.html', locals())


def contacts_page(request):
    return render(request, 'contacts.html', locals())


def products(request, name):
    return render(request, 'products/' + name + '.html', locals())


@csrf_exempt
def send_email(request):
    message = 'Номер телефона: ' + str(request.POST['phone'])
    email = EmailMessage('Запрос на обратный звонок', message, to=['info@payflex.ru'])
    email.send()
    return HttpResponse('MF000')

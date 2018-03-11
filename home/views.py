import requests
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from payflex import settings


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


@csrf_exempt
def send_email_contacts(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    if result['success']:
        message = 'Номер телефона: ' + str(request.POST['phone'])
        email = EmailMessage('Запрос на обратный звонок', message, to=['info@payflex.ru'])
        email.send()
        return HttpResponse('MF000')
    else:
        return HttpResponse('MF001')

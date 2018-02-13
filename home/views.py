from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html', locals())


def contacts_page(request):
    return render(request, 'contacts.html', locals())


def products(request, name):
    return render(request, 'products/' + name + '.html', locals())

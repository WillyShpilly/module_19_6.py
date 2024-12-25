from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def news(request):
    posts = News.objects.all().order_by('-created_at')
    elements_in_page = request.GET.get('elements_in_page', 3)
    paginator = Paginator(posts, per_page=elements_in_page)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'page_posts': page_posts,
        'elements_in_page': elements_in_page
    }
    return render(request, 'news.html', context)


def shopping_cart(request):
    text = 'Корзина'
    text2 = 'Извините, ваша корзина пуста'
    context = {
        'text': text,
        'text2': text2
    }
    return render(request, 'shopping_cart.html', context)


def shop(request):
    text = 'Игрища'
    games = Games.objects.all()
    context = {
        'text': text,
        'games': games
    }
    return render(request, 'shop.html', context)


def main_page(request):
    text = 'Главная страница'
    context = {
        'text': text
    }
    return render(request, 'main_page.html', context)


def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    users = [i.name for i in buyers]
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
        'users': users,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'error1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'error2': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'error3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'registration_page.html', context)
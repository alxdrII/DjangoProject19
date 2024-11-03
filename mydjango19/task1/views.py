from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def game_products(request):
    from .models import Game
    context = {'games': Game.objects.all()}

    return render(request, 'games.html', context)


def sign_up_by_django(request):
    from .models import Buyer

    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            elif len(Buyer.objects.filter(name=username)) > 0:
                info['error'] = 'Пользователь уже существует'

            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'<h2 align="center">Приветствуем, {username}!</h2>')

    else:
        form = UserRegister()

    return render(request, 'registration_page1.html', {'form': form, 'info': info})

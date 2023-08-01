from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Вы успешно зарегистрировались! Можете войти в аккаунт.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Blog - Registration',
    }

    return render(request=request, template_name='users/register.html', context=context)


@login_required()
def profile(request):
    context = {
        'title': 'Blog - Profile'
    }
    return render(request=request, template_name='users/profile.html', context=context)

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .forms import UserRegisterForm, UserLoginForm


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



# def login(request):
#     if request.POST:
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index:blog-home'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'form': form,
#         'title': 'Blog - Login',
#     }
#
#     return render(request=request, template_name='users/login.html', context=context)





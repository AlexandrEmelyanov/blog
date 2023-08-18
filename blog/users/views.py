from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin

from .forms import UserProfileForm, UserRegisterForm
from .models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    title = 'Blog - Registration'
    success_message = 'Вы успешно зарегистрировались! Выполните вход в аккаунт.'
    success_url = reverse_lazy('users:login')


class UserProfileView(TitleMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Blog - Profile'
    success_message = 'Данные успешно изменены.'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


# @login_required()
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Данные успешно изменены.')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {
#         'title': 'Blog - Profile',
#         'form': form,
#     }
#
#     return render(request=request, template_name='users/profile.html', context=context)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Вы успешно зарегистрировались! Выполните вход в аккаунт.')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#
#     context = {
#         'form': form,
#         'title': 'Blog - Registration',
#     }
#
#     return render(request=request, template_name='users/register.html', context=context)

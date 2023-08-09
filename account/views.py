from django.shortcuts import render
from django.views.generic import CreateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from . import forms

# Create your views here.


def account_index(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'index.html', {'user': user})
    else:
        return render(request, 'index.html', {'user': None})


class SignUpView(CreateView):
    template_name = "register.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy('account:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


class LoginView(LoginView):
    template_name = "login.html"
    form_class = forms.LoginForm


class LogoutView(LogoutView):
    template_name = "logout.html"

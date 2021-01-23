from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView, CreateView
from django.urls import reverse
from django.shortcuts import redirect

from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('accounts:base')
        return next_url

class BaseView(TemplateView):

    template_name = 'index.html'

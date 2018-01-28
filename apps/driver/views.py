from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import FormView, RedirectView

from apps.customer.models import Customer
from apps.driver.forms.forms import DriverSignUpForm, UpdateDriverForm
from apps.driver.models import Driver


class SignupView(generic.CreateView):
    form_class = DriverSignUpForm
    success_url = '/driver/login/'
    template_name = 'driver_signup.html'


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = 'driver_home'
    template_name = 'driver_login.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = 'home.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateDriverForm
    success_url = 'driver_home.html'
    template_name = 'driver_update_profile.html'
    model = Driver

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

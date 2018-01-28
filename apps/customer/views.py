from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import FormView, RedirectView

from apps.customer.forms.forms import CustomerSignUpForm
from apps.customer.models import Customer
from apps.customer.forms.forms import UpdateCustomerForm


class SignupView(generic.CreateView):
    form_class = CustomerSignUpForm
    success_url = '/customer/login/'
    template_name = 'customersignup.html'


class LoginView(FormView):
    success_url = 'customer_home.html'
    form_class = AuthenticationForm
    template_name = 'customerlogin.html'

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
    form_class = UpdateCustomerForm
    success_url = 'customer_home.html'
    template_name = 'customerupdateprofile.html'
    model = Customer

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

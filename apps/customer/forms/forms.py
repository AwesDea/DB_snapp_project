from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from apps.customer.models import Customer


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    phone_number = forms.IntegerField(required=True)
    name = forms.CharField(max_length=10)
    family = forms.CharField(max_length=16)
    gender = forms.IntegerField()
    birthday = forms.IntegerField()
    address = forms.IntegerField()

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Customer(phone_number=None,
                               gender=None,
                               birthday=None,
                               address=None,
                               credit=0)
            profile.phone_number = self.cleaned_data['phone_number']
            profile.gender = self.cleaned_data['gender']
            profile.birthday = self.cleaned_data['birthday']
            profile.address = self.cleaned_data['address']
            profile.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                  'phone_number', 'gender', 'birthday', 'address')


class UpdateCustomerForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(required=False, widget=forms.PasswordInput)

    phone_number = forms.IntegerField(required=True)
    name = forms.CharField(max_length=10)
    family = forms.CharField(max_length=16)
    gender = forms.IntegerField()
    birthday = forms.IntegerField()
    address = forms.IntegerField()

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            self.add_error('password1', 'password error')

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = user.customer_profile

        if commit:
            user.save()
            profile.save()
        return profile

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'password1', 'password2',
                  'phone_number', 'gender', 'birthday', 'address')

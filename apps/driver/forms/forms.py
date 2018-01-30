from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from apps.customer.models import Driver


class DriverSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')

    acc_num = forms.IntegerField(required=True)
    father_name = forms.CharField(max_length=10)
    national_code = forms.IntegerField(required=True)
    is_ready_field = forms.NullBooleanField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = forms.CharField(max_length=30)

    lat = forms.IntegerField()
    lng = forms.IntegerField()

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Driver(user=user,acc_num=None,
                             father_name=None,
                             national_code=None,
                             is_ready_field=None,
                             address=None,
                             lat=None,
                             lng=None, )
            profile.acc_num = self.cleaned_data['acc_num']
            profile.father_name = self.cleaned_data['father_name']
            profile.national_code = self.cleaned_data['national_code']
            profile.is_ready_field = self.cleaned_data['is_ready_field']
            profile.address = self.cleaned_data['address']
            profile.lat = self.cleaned_data['lat']
            profile.lng = self.cleaned_data['lng']
            profile.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                                                                               'acc_num', 'father_name',
                  'national_code', 'is_ready_field', 'address', 'lat', 'lng')


class UpdateDriverForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(required=False, widget=forms.PasswordInput)
    acc_num = forms.IntegerField(required=True)
    father_name = forms.CharField(max_length=10)
    national_code = forms.IntegerField(required=True)
    is_ready_field = forms.NullBooleanField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = forms.CharField(max_length=30)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            self.add_error('password1', 'password error')

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = user.driver_profile

        if commit:
            user.save()
            profile.save()
        return profile

    class Meta:
        model = Driver
        fields = ( 'first_name', 'last_name', 'password1', 'password2',
                                                                               'acc_num', 'father_name',
                  'national_code', 'is_ready_field', 'address', 'lat', 'lng')

from django import forms
from django.contrib.auth.models import User
from . import models


from django.core.validators import RegexValidator
from .models import User, Customer


from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django import forms
from .models import User, Customer

from django.core.validators import RegexValidator
from django import forms
from .models import User, Customer

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django import forms
from django.core.exceptions import ValidationError
from .models import User, Customer

class CustomerUserForm(forms.ModelForm):
    username = forms.CharField(validators=[MaxLengthValidator(10, 'Username must be at most 10 characters.')])
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }



class CustomerForm(forms.ModelForm):
    address = forms.CharField(max_length=15)
    mobile = forms.IntegerField(validators=[
        MinValueValidator(1000000000, 'Mobile number must be 10 digits.'),
        MaxValueValidator(9999999999, 'Mobile number must be 10 digits.')
    ])


    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(str(mobile)) != 10:
            raise ValidationError('Mobile number must be 10 digits.')
        return mobile

    password = forms.CharField(widget=forms.PasswordInput(), validators=[
        MinLengthValidator(6, 'Password must be at least 6 characters.')
    ])

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password[0].isupper():
            raise ValidationError('Password must start with a capital letter.')
        return password

    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'profile_pic']


class TasksForm(forms.ModelForm):
        class Meta:
            model=models.Tasks
            fields=['name','date']
    


from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'certificate_file']


from django import forms
from django.contrib.auth.models import User
from .models import Customer

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'password']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', 'address', 'mobile']

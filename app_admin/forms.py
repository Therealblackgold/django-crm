from django import forms
from accounts.models import Member
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from app_admin.models import Payment

# class UpdateMemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         # fields = '__all__'
#         exclude = ('user', )

STATUS_CHOICES = [
    ('pending', 'pending'),
    ('active', 'active'),
    ('cancelled', 'cancelled'),
]


class UpdateMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = (
            'first_name',
            'last_name',
            'id_number',
            'status',
            'phone_number',
            'phone_number_2',
            'email',
            'package',
            'address',
            'id_copy',
            'proof_of_address',
        )

        widgets = {
            'first_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'id_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Number'
            }),
            'email':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@thuso.com'
            }),
            'phone_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'phone_number_2':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'address':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Street'
            }),
        }


class UpdatePendingMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = (
            'first_name',
            'last_name',
            'id_number',
            'status',
            'phone_number',
            'phone_number_2',
            'email',
            'package',
            'address',
            'id_copy',
            'proof_of_address',
        )

        widgets = {
            'first_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'id_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Number'
            }),
            'email':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@christian.com'
            }),
            'phone_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'phone_number_2':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'address':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
        }


# Admin user registration
class AdminMemberCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Member
        fields = [
            'status',
            'recieved_by',
            'first_name',
            'last_name',
            'username',
            'id_number',
            'email',
            'phone_number',
            'phone_number_2',
            'package',
            'address',
            'password1',
            'password2',
            'id_copy',
            'proof_of_address',
        ]


class AddMemberPayment(ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'month', 'proof_of_payment']
        widgets = {
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

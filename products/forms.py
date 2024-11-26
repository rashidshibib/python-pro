from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Product, Contact  # تأكد من استيراد النماذج الأخرى التي تحتاجها

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')  # أو أي حقول أخرى ترغب بها

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'title', 'description', 'price', 'download_file', 'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

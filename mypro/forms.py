from django import forms
from .models import Product  # افترض أن لديك نموذج Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']  # اضبط الحقول حسب الحاجة

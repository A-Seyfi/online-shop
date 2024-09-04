from django import forms
from .models import Product

class ProductCompareForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="محصولی برای مقایسه انتخاب کنید",
    )
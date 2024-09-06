from django import forms
from .models import Product, Color, RAM, Storage, Warranty

class ProductCompareForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="محصولی برای مقایسه انتخاب کنید",
    )

class LaptopSelectionForm(forms.Form):
    color = forms.ModelChoiceField(queryset=Color.objects.none(), label="رنگ محصول")
    ram = forms.ModelChoiceField(queryset=RAM.objects.none(), label="رم محصول")
    storage = forms.ModelChoiceField(queryset=Storage.objects.none(), label="حافظه محصول")
    warranty = forms.ModelChoiceField(queryset=Warranty.objects.none(), label="گارانتی محصول")

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop("product_id", None)
        super().__init__(*args, **kwargs)
        if self.product_id:
            try:
                product_id = int(self.product_id)
                self.fields['color'].queryset = Color.objects.filter(product_id=product_id)
                self.fields['ram'].queryset = RAM.objects.filter(product_id=product_id)
                self.fields['storage'].queryset = Storage.objects.filter(product_id=product_id)
                self.fields['warranty'].queryset = Warranty.objects.filter(product_id=product_id)
            except (ValueError, TypeError):
                pass
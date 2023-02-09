from django import forms

class ClothesForm(forms.Form):
    name = forms.CharField(max_length =100)
    type = forms.CharField(max_length = 100)
    price = forms.FloatField()
    stock = forms.BooleanField()
    product_image = forms.ImageField()
    size = forms.CharField(max_length = 10)

    


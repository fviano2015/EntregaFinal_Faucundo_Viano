from django.shortcuts import render
from Shop.forms import ClothesForm
from Shop.models import Clothes

def create_clothes(request):
    if request.method == 'GET':
        context = {'form': ClothesForm()}
        return render(request, 'Shop/create-clothes.html', context = context)
    elif request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            Clothes.objects.create(
                name = form.cleaned_data['name'],
                type = form.cleaned_data['type'],
                price = form.cleaned_data['price'],
                product_image = form.cleaned_data['product_image'],
                size = form.cleaned_data['size'],
                stock = form.cleaned_data['stock'],
            )
            context = {
                'message' : "Ropa creada exitosamente"
            } 
            return render(request, 'Shop/create-clothes.html', context = context)
        else:
            context = {
                'form errors': form.errors,
                'form' : ClothesForm()
                }
        return render(request, 'Shop/create-clothes.html', context = context)



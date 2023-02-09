from django.contrib import admin
from Shop.models import Clothes

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'price', 'stock', 'product_image', 'size')
    list_filter = ("stock", 'type', "price", 'product_image', 'size')
    search_fields = ("name", 'type')

from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display="id","nombre","descripcion","precio","imagen"

    def foto(self, obj):
        return format_html('<img src={} />', obj.imagen.url)



admin.site.register(Producto,ProductoAdmin)
from django.contrib import admin
from . import models

# admin.site.register(models.Brand)
admin.site.register(models.Car)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}
    list_display = ['brand_name', 'slug']

admin.site.register(models.Brand, BrandAdmin)

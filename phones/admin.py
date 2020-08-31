from django.contrib import admin

from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date')


admin.site.register(Phone, PhoneAdmin)

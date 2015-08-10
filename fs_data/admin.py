from django.contrib import admin

from .models import Country, Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'country', 'zip_code', 'town', 'amount')


admin.site.register(Country)
admin.site.register(Payment, PaymentAdmin)


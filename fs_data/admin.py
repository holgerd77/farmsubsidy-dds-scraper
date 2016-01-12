from __future__ import unicode_literals
from django.contrib import admin

from .models import Agency, Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'zip_code', 'town', 'year', 'amount_nc', 'amount_euro',)


admin.site.register(Agency)
admin.site.register(Payment, PaymentAdmin)


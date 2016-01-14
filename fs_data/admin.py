from __future__ import unicode_literals
from django.contrib import admin

from .models import Agency, Payment


def shorten_url(url):
    max_length = 40
    return (url[:max_length] + '..') if len(url) > max_length else url


class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', '_info_url', '_scrape_url',)
    
    def _info_url(self, instance):
        return '<a href="{url}" target="_blank">{url_short}</a>'.format(
            url=instance.info_url, url_short=shorten_url(instance.info_url))
    
    _info_url.allow_tags = True
    
    def _scrape_url(self, instance):
        return '<a href="{url}" target="_blank">{url_short}</a>'.format(
            url=instance.scrape_url, url_short=shorten_url(instance.scrape_url))
    
    _scrape_url.allow_tags = True
        

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'zip_code', 'town', 'year', 'amount_nc', 'amount_euro',)


admin.site.register(Agency, AgencyAdmin)
admin.site.register(Payment, PaymentAdmin)


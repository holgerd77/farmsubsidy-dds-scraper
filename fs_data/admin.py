from __future__ import unicode_literals
from django.contrib import admin

from .models import Country, Payment


def shorten_url(url):
    max_length = 40
    return (url[:max_length] + '..') if len(url) > max_length else url


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'name', 'agency_name', '_info_url', '_data_url', '_scrape_url',)
    
    def _info_url(self, instance):
        return '<a href="{url}" target="_blank">{url_short}</a>'.format(
            url=instance.info_url, url_short=shorten_url(instance.info_url))
    
    _info_url.allow_tags = True
    
    def _data_url(self, instance):
        return '<a href="{url}" target="_blank">{url_short}</a>'.format(
            url=instance.data_url, url_short=shorten_url(instance.data_url))
    
    _data_url.allow_tags = True
    
    def _scrape_url(self, instance):
        return '<a href="{url}" target="_blank">{url_short}</a>'.format(
            url=instance.scrape_url, url_short=shorten_url(instance.scrape_url))
    
    _scrape_url.allow_tags = True
        

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'zip_code', 'town', 'year', 'amount_nc', 'amount_euro',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Payment, PaymentAdmin)


from django.db import models
from dynamic_scraper.models import Scraper
from scrapy.contrib.djangoitem import DjangoItem


class Agency(models.Model):
    country = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=200)
    info_url = models.URLField()
    scrape_url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return '{name} (country)'.format(name=self.name, country=self.country)


class Payment(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=30, blank=True)
    town = models.CharField(max_length=200)
    region = models.CharField(max_length=200, blank=True)
    year = models.IntegerField()
    sub_payments = models.TextField(blank=True)
    amount_nc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    nc_symbol = models.CharField(max_length=3, blank=True)
    nc_conv_date = models.DateTimeField(blank=True, null=True)
    nc_conv_rate = models.DecimalField(max_digits=10, decimal_places=4)
    amount_euro = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return "%s [%s|%d]" % (self.recipient, self.country, self.amount)


class PaymentItem(DjangoItem):
    django_model = Payment
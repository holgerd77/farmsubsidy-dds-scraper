from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from dynamic_scraper.models import Scraper
import scrapy
from scrapy.contrib.djangoitem import DjangoItem


class Agency(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, primary_key=True, help_text="Two-letter country code (e.g. 'BE', 'CZ', 'PL')")
    info_url = models.URLField()
    scrape_url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    comments = models.TextField(blank=True)

    def __str__(self):
        return '{name} (country)'.format(name=self.name, country=self.country)


class Payment(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, help_text="Two-letter country code (e.g. 'BE', 'CZ', 'PL')")
    zip_code = models.CharField(max_length=30, blank=True)
    town = models.CharField(max_length=200)
    region = models.CharField(max_length=200, blank=True)
    year = models.IntegerField()
    amount_nc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    nc_symbol = models.CharField(max_length=3, blank=True)
    nc_sign = models.CharField(max_length=6, blank=True)
    nc_conv_date = models.DateTimeField(blank=True, null=True)
    nc_conv_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    sub_payments_nc = models.TextField(blank=True)
    sub_payments_euro = models.TextField(blank=True)
    amount_euro = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return "%s [%s|%d]" % (self.recipient, self.country, self.amount)


def sps_str2list(sps_str):
    if not sps_str or sps_str == '':
        return {}
    tmp_sps_list = [x.strip().split(',') for x in sps_str.split('|')]
    sps_list = []
    for tmp_sp_list in tmp_sps_list:
        name = tmp_sp_list[0]
        amount = round(float(tmp_sp_list[1]), 2)
        sps_list.append({
            'name': name,
            'amount': amount,
        })
    return sps_list


def serialize_sps(sps_list):
    return sps_list


def serialize_sps_nc(sps_str):
    sps_list = sps_str2list(sps_str)
    return serialize_sps(sps_list)


def serialize_sps_euro(sps_str):
    conv = False
    if 'CONV' in sps_str:
        pos = sps_str.find('CONV')
        conv_rate = sps_str[0:pos]
        sps_str = sps_str[pos+4:]
        conv = True
    sps_list = sps_str2list(sps_str)
    if conv:
        for payment in sps_list:
            payment['amount'] = round(float(payment['amount']) / float(conv_rate), 2)
    return serialize_sps(sps_list)


class PaymentItem(DjangoItem):
    django_model = Payment
    sub_payments_nc = scrapy.Field(serializer=serialize_sps_nc)
    sub_payments_euro = scrapy.Field(serializer=serialize_sps_euro)

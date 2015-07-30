from django.db import models
from dynamic_scraper.models import Scraper
from scrapy.contrib.djangoitem import DjangoItem


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=200)
    public_body_url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Payment(models.Model):
    recipient = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    zip_code = models.CharField(max_length=30)
    town = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return "%s [%s|%d]" % (self.recipient, self.country, self.amount)


class PaymentItem(DjangoItem):
    django_model = Payment
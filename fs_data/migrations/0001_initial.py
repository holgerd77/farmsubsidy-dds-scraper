# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0015_added_datetime_fields_for_last_scraper_save_and_checker_delete_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('country', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('info_url', models.URLField()),
                ('scrape_url', models.URLField()),
                ('comments', models.TextField(blank=True)),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=30, blank=True)),
                ('town', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200, blank=True)),
                ('year', models.IntegerField()),
                ('sub_payments', models.TextField(blank=True)),
                ('amount_nc', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('nc_symbol', models.CharField(max_length=3, blank=True)),
                ('nc_conv_date', models.DateTimeField(null=True, blank=True)),
                ('nc_conv_rate', models.DecimalField(max_digits=10, decimal_places=4)),
                ('amount_euro', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
    ]

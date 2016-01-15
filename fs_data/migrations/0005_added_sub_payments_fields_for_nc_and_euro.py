# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_data', '0004_making_nc_conv_rate_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='sub_payments_euro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='sub_payments_nc',
            field=models.TextField(blank=True),
        ),
    ]

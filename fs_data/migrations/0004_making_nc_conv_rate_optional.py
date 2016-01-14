# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_data', '0003_making_nc_conv_rate_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='nc_conv_rate',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
        ),
    ]

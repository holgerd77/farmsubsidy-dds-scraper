# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_data', '0002_remove_sub_payments_in_favour_of_schemaless_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='nc_conv_rate',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4),
        ),
    ]

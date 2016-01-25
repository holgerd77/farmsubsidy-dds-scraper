# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_data', '0005_added_sub_payments_fields_for_nc_and_euro'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='nc_sign',
            field=models.CharField(max_length=6, blank=True),
        ),
    ]

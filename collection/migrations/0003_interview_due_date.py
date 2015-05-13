# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_interview_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 12, 23, 19, 29, 829051, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('total_quantity', models.DecimalField(max_digits=10, decimal_places=2)),
                ('customer', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=10)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='invoice',
            name='transaction',
            field=models.ManyToManyField(to='customer.Transaction'),
            preserve_default=True,
        ),
    ]

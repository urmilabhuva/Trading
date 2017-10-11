# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField(verbose_name=[b'%Y-%m-%d'])),
                ('end_date', models.DateField(verbose_name=[b'%Y-%m-%d'])),
                ('warehouse1', models.CharField(max_length=250, blank=True)),
                ('store1', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse2', models.CharField(max_length=250, blank=True)),
                ('store2', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse3', models.CharField(max_length=250, blank=True)),
                ('store3', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse4', models.CharField(max_length=250, blank=True)),
                ('store4', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse5', models.CharField(max_length=250, blank=True)),
                ('store5', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse6', models.CharField(max_length=250, blank=True)),
                ('store6', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse7', models.CharField(max_length=250, blank=True)),
                ('store7', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse8', models.CharField(max_length=250, blank=True)),
                ('store8', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse9', models.CharField(max_length=250, blank=True)),
                ('store9', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse10', models.CharField(max_length=250, blank=True)),
                ('store10', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse11', models.CharField(max_length=250, blank=True)),
                ('store11', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse12', models.CharField(max_length=250, blank=True)),
                ('store12', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse13', models.CharField(max_length=250, blank=True)),
                ('store13', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse14', models.CharField(max_length=250, blank=True)),
                ('store14', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('warehouse15', models.CharField(max_length=250, blank=True)),
                ('store15', models.DecimalField(default=100, null=True, max_digits=5, decimal_places=2)),
                ('like', models.CharField(max_length=50, choices=[(b'select1', b'All Weather'), (b'select2', b'Aggressive')])),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGuest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventGuestResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_guest', models.ForeignKey(to='app.EventGuest')),
            ],
        ),
        migrations.CreateModel(
            name='EventHost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('style', models.CharField(max_length=250)),
                ('abv', models.DecimalField(max_digits=3, decimal_places=1)),
                ('producer', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_list', models.CommaSeparatedIntegerField(max_length=250)),
                ('best_product', models.ForeignKey(to='app.EventProduct')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='eventproduct',
            name='event',
            field=models.ForeignKey(to='app.Event'),
        ),
        migrations.AddField(
            model_name='eventproduct',
            name='product',
            field=models.ForeignKey(to='app.Product'),
        ),
        migrations.AddField(
            model_name='eventhost',
            name='event',
            field=models.ForeignKey(to='app.Event'),
        ),
        migrations.AddField(
            model_name='eventhost',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventguestresponse',
            name='response',
            field=models.ForeignKey(to='app.Response'),
        ),
        migrations.AddField(
            model_name='eventguest',
            name='event',
            field=models.ForeignKey(to='app.Event'),
        ),
        migrations.AddField(
            model_name='eventguest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

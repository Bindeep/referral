# Generated by Django 3.0.7 on 2020-08-02 06:53

import apps.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, default='')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50, validators=[apps.core.validators.validate_phone_number])),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('progress', 'Progress'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('commission_amount', models.FloatField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='common.City')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='company.Company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='company.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='referral.Referral')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

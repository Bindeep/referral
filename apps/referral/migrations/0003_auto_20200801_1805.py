# Generated by Django 3.0.7 on 2020-08-01 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_user'),
        ('referral', '0002_referral_referrer'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='commission_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='referral',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='company.Company'),
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
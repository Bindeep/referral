# Generated by Django 3.0.7 on 2020-08-02 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referral', '0001_initial'),
        ('referrer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='referrer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='referrer.Referrer'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-18 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='payment_status',
        ),
    ]
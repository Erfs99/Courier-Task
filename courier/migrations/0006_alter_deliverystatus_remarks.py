# Generated by Django 4.0 on 2022-01-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0005_alter_deliverydetails_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverystatus',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
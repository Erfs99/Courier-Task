# Generated by Django 4.0 on 2022-01-04 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=45)),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourierMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=30)),
                ('national_id', models.CharField(max_length=40)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('additional_salary', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('reduce_salary', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('package_type', models.CharField(choices=[('perishable', 'Perishable'), ('fragile', 'Fragile'), ('document', 'Document'), ('others', 'Others')], max_length=20)),
                ('package_weight', models.IntegerField()),
                ('from_address', models.CharField(max_length=150)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('courier_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courierman')),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courier.address')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('status', models.CharField(choices=[('Received', 'Received'), ('Dispatched', 'Dispatched'), ('Processing', 'Processing')], max_length=20)),
                ('courier_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courierman')),
                ('details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courier.deliverydetails')),
            ],
        ),
        migrations.AddField(
            model_name='deliverydetails',
            name='receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courier.receiver'),
        ),
    ]

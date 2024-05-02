# Generated by Django 4.1.5 on 2024-03-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_app', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountNumber', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('openDate', models.DateField()),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cardType', models.CharField(max_length=50)),
                ('cardNumber', models.CharField(max_length=50)),
                ('cvv', models.CharField(max_length=5)),
                ('expDate', models.CharField(max_length=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

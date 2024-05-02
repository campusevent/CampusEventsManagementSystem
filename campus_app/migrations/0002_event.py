# Generated by Django 4.1.5 on 2024-03-17 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('eventAddDate', models.DateField(auto_now_add=True)),
                ('eventType', models.CharField(max_length=50)),
                ('eventTitle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('eventposter', models.CharField(max_length=150)),
                ('eventDateTime', models.DateTimeField()),
                ('eventLocation', models.CharField(max_length=200)),
                ('eventFee', models.FloatField()),
                ('totalAttendees', models.IntegerField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus_app.user')),
            ],
        ),
    ]

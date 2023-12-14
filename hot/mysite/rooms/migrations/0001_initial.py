# Generated by Django 5.0 on 2023-12-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(verbose_name='Номер комнаты')),
                ('room_resident', models.CharField(max_length=100, verbose_name='Имя резидента')),
                ('room_status', models.CharField(max_length=40, verbose_name='Статус комнаты')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
    ]
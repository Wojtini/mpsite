# Generated by Django 3.2.12 on 2022-02-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TankExpectations',
            fields=[
                ('tank_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exp_Def', models.FloatField()),
                ('exp_Frag', models.FloatField()),
                ('exp_Spot', models.FloatField()),
                ('exp_Damage', models.FloatField()),
                ('exp_WinRate', models.FloatField()),
            ],
        ),
    ]
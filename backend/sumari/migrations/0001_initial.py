# Generated by Django 4.1.2 on 2022-10-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sumari',
            fields=[
                ('SumarId', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
    ]
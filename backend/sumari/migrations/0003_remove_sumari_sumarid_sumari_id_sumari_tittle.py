# Generated by Django 4.1.2 on 2022-10-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumari', '0002_alter_sumari_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sumari',
            name='SumarId',
        ),
        migrations.AddField(
            model_name='sumari',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sumari',
            name='tittle',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

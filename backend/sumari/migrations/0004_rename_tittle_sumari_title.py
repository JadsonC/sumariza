# Generated by Django 4.1.2 on 2022-10-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumari', '0003_remove_sumari_sumarid_sumari_id_sumari_tittle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sumari',
            old_name='tittle',
            new_name='title',
        ),
    ]

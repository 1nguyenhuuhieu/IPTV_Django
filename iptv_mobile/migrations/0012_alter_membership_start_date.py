# Generated by Django 3.2 on 2021-07-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_mobile', '0011_alter_group_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

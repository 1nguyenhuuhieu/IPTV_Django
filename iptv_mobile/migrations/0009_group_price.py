# Generated by Django 3.2 on 2021-07-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_mobile', '0008_alter_membership_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_mobile', '0002_auto_20210704_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='cover',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_mobile', '0005_alter_stream_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

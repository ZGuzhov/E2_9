# Generated by Django 3.1 on 2020-10-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_emails', '0003_auto_20200930_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillist',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
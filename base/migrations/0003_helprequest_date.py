# Generated by Django 4.2.2 on 2023-08-10 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_helprequest_days_alter_helprequest_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
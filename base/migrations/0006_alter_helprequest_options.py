# Generated by Django 4.2.2 on 2023-08-11 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_helprequest_options_helprequest_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='helprequest',
            options={'ordering': ['-date']},
        ),
    ]

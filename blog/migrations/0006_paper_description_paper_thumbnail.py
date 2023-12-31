# Generated by Django 4.2.2 on 2023-08-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_paper_delete_essay_delete_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='thumbnail',
            field=models.FileField(default='i am a description', upload_to='thumbnails/'),
            preserve_default=False,
        ),
    ]

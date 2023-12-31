# Generated by Django 4.2.2 on 2023-09-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_paper_price_paper_pages_alter_paper_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='paper',
            name='topic',
            field=models.CharField(choices=[('E', 'Education'), ('D', 'Development'), ('L', 'Leadership'), ('R', 'Research'), ('H', 'History'), ('E', 'Economics'), ('B', 'Business'), ('S', 'Sports'), ('F', 'Farminig'), ('N', 'Nursing'), ('A', 'Accounting'), ('F', 'Finance'), ('M', 'Marketing'), ('C', 'Calculus'), ('P', 'Proposals'), ('PR', 'Proof reading'), ('BM', 'Business management'), ('HR', 'Human Resource'), ('SC', 'Supply chain & logistics'), ('TS', 'Thesis'), ('CP', 'Concept Papers'), ('BP', 'Business Plans'), ('SM', 'Strategic management'), ('DA', 'Data analysis'), ('OT', 'Online Tutor')], max_length=100),
        ),
    ]

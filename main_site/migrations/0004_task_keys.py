# Generated by Django 3.1.1 on 2020-10-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20201014_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='keys',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

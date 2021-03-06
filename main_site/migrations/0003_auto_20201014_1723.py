# Generated by Django 3.1.1 on 2020-10-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20201008_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='similarity',
            new_name='similarity_score',
        ),
        migrations.AddField(
            model_name='homework',
            name='text_keys',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='text_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='homework',
            name='text_score',
            field=models.IntegerField(default=0),
        ),
    ]

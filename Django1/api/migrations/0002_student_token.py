# Generated by Django 4.0.1 on 2022-02-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='token',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]

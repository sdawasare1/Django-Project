# Generated by Django 4.0.1 on 2022-02-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
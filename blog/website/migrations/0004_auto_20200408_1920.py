# Generated by Django 3.0.4 on 2020-04-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
        migrations.AddField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
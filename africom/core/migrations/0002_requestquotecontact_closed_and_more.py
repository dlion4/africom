# Generated by Django 4.2.11 on 2024-04-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestquotecontact',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='requestquotecontact',
            name='package',
            field=models.CharField(max_length=1),
        ),
    ]

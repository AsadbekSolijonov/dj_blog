# Generated by Django 5.2.3 on 2025-06-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=1212, unique=True),
            preserve_default=False,
        ),
    ]

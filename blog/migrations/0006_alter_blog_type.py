# Generated by Django 5.2.3 on 2025-06-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.CharField(choices=[('Jounal', 'Journal'), ('Life updates', 'Life updates'), ('Travel stories', 'Travel stories'), ('Personal growth', 'Personal growth')], default='Jounal', max_length=50),
        ),
    ]

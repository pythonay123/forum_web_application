# Generated by Django 3.0.5 on 2020-04-15 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_auto_20200415_0311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'ordering': ['section_name']},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['posted_date']},
        ),
    ]

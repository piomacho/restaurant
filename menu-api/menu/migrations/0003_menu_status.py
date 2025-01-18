# Generated by Django 5.1.5 on 2025-01-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_menu_author_menu_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
    ]

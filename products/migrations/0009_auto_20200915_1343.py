# Generated by Django 3.1.1 on 2020-09-15 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200915_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='slugf',
        ),
    ]
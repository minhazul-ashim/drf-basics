# Generated by Django 5.0.3 on 2024-03-29 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_upload_alter_useraccount_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='upload',
            new_name='resume',
        ),
    ]
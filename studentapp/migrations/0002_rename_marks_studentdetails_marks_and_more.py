# Generated by Django 4.1 on 2022-09-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetails',
            old_name='Marks',
            new_name='marks',
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
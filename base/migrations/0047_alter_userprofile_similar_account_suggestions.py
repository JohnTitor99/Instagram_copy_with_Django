# Generated by Django 4.0.4 on 2022-07-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_alter_userprofile_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='similar_account_suggestions',
            field=models.BooleanField(default=True),
        ),
    ]

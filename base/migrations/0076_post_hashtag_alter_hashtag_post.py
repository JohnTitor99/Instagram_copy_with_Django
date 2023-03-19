# Generated by Django 4.0.4 on 2022-10-01 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0075_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(related_name='hashtag_posts', to='base.hashtag'),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtags', to='base.post'),
        ),
    ]

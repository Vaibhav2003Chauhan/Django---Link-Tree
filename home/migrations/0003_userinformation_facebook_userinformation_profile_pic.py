# Generated by Django 4.2.1 on 2023-08-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userinformation_gfg_userinformation_leetcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='facebook',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=''),
        ),
    ]

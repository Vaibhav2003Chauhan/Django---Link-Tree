# Generated by Django 4.2.1 on 2023-09-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userinformation_role_alter_userinformation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='profile_pic',
            field=models.ImageField(default='profile.jpg', null=True, upload_to=''),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_userinformation_gfg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='GFG',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='LeetCode',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='Linkedin',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='Resume',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='codechef',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='codepen',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='description',
            field=models.TextField(default='------', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='facebook',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='github',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='hackerrank',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='insta',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='mail',
            field=models.CharField(default='------', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='name',
            field=models.CharField(default='------', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='phone',
            field=models.CharField(default='------', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='portfolio',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='role',
            field=models.CharField(default='------', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='twitter',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='website',
            field=models.CharField(default='------', max_length=600, null=True),
        ),
    ]

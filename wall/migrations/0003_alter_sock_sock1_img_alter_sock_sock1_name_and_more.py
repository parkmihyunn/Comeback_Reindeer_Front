# Generated by Django 4.1.3 on 2022-12-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_alter_sock_sock1_img_alter_sock_sock1_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sock',
            name='sock1_img',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock1_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock2_img',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock2_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock3_img',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock3_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
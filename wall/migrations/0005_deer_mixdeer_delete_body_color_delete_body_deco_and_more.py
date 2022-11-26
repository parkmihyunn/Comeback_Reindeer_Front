# Generated by Django 4.1.3 on 2022-11-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_rename_body_eco_body_deco_delete_deer'),
    ]

    operations = [
        migrations.CreateModel(
            name='deer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horn', models.CharField(max_length=200)),
                ('hair', models.CharField(max_length=200)),
                ('eye', models.CharField(max_length=200)),
                ('body_color', models.CharField(max_length=200)),
                ('body_deco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='mixDeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horn', models.CharField(max_length=200)),
                ('hair', models.CharField(max_length=200)),
                ('eye', models.CharField(max_length=200)),
                ('body_color', models.CharField(max_length=200)),
                ('body_deco', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='body_color',
        ),
        migrations.DeleteModel(
            name='body_deco',
        ),
        migrations.DeleteModel(
            name='eye',
        ),
        migrations.DeleteModel(
            name='hair',
        ),
        migrations.DeleteModel(
            name='horn',
        ),
    ]

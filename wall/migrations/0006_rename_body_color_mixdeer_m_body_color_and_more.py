# Generated by Django 4.1.3 on 2022-11-25 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_deer_mixdeer_delete_body_color_delete_body_deco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mixdeer',
            old_name='body_color',
            new_name='m_body_color',
        ),
        migrations.RenameField(
            model_name='mixdeer',
            old_name='body_deco',
            new_name='m_body_deco',
        ),
        migrations.RenameField(
            model_name='mixdeer',
            old_name='eye',
            new_name='m_eye',
        ),
        migrations.RenameField(
            model_name='mixdeer',
            old_name='hair',
            new_name='m_hair',
        ),
        migrations.RenameField(
            model_name='mixdeer',
            old_name='horn',
            new_name='m_horn',
        ),
    ]

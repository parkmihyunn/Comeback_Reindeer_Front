<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-12-08 06:22
=======
# Generated by Django 4.1.3 on 2022-12-13 17:29
>>>>>>> 484da55050583991e0adfa141bae607a9b085fea

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
<<<<<<< HEAD
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='wreath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=200)),
                ('width', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_wreath', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to=settings.AUTH_USER_MODEL)),
=======
            name='Sock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sock1_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sock1_img', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sock2_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sock2_img', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sock3_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sock3_img', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('user_id', models.ForeignKey(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_sock', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealWreath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orn1', models.SmallIntegerField(default=-1)),
                ('orn2', models.SmallIntegerField(default=-1)),
                ('orn3', models.SmallIntegerField(default=-1)),
                ('orn4', models.SmallIntegerField(default=-1)),
                ('orn5', models.SmallIntegerField(default=-1)),
                ('orn6', models.SmallIntegerField(default=-1)),
                ('orn7', models.SmallIntegerField(default=-1)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_RealWreath', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrnamentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src1', models.CharField(default=-1, max_length=50)),
                ('src2', models.CharField(default=-1, max_length=50)),
                ('src3', models.CharField(default=-1, max_length=50)),
                ('src4', models.CharField(default=-1, max_length=50)),
                ('src5', models.CharField(default=-1, max_length=50)),
                ('src6', models.CharField(default=-1, max_length=50)),
                ('src7', models.CharField(default=-1, max_length=50)),
                ('src8', models.CharField(default=-1, max_length=50)),
                ('src9', models.CharField(default=-1, max_length=50)),
                ('src10', models.CharField(default=-1, max_length=50)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_ornament', to=settings.AUTH_USER_MODEL, unique=True)),
>>>>>>> 484da55050583991e0adfa141bae607a9b085fea
            ],
        ),
        migrations.CreateModel(
            name='mixDeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_horn', models.CharField(max_length=200)),
                ('m_hair', models.CharField(max_length=200)),
                ('m_eye', models.CharField(max_length=200)),
                ('m_body_color', models.CharField(max_length=200)),
                ('m_body_deco', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_deer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

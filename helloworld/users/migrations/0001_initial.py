# Generated by Django 4.0.3 on 2022-03-18 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Admin', max_length=10)),
                ('notifications', models.CharField(default=None, max_length=400000)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('Sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('desc', models.CharField(max_length=400)),
                ('price', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField(default=None)),
                ('gender', models.CharField(max_length=2)),
                ('address', models.CharField(default=None, max_length=40000)),
                ('country', models.CharField(default='India', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ImageField(upload_to='')),
                ('f1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(default=None, max_length=400000)),
                ('fm1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mf1', to='users.users')),
                ('fm2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mf2', to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=None)),
                ('f1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend1', to='users.users')),
                ('f2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend2', to='users.users')),
            ],
        ),
    ]
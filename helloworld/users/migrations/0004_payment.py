# Generated by Django 4.0.3 on 2022-03-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.IntegerField(max_length=16)),
                ('cvv', models.IntegerField(max_length=3)),
                ('mm', models.IntegerField(max_length=2)),
                ('yy', models.IntegerField(max_length=2)),
                ('name', models.CharField(default=None, max_length=40)),
                ('pay1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_payment_id_alter_payment_pay1'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay1',
            field=models.IntegerField(auto_created=True),
        ),
    ]
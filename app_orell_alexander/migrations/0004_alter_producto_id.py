# Generated by Django 4.2.1 on 2023-06-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orell_alexander', '0003_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

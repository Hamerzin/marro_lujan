# Generated by Django 4.0.4 on 2022-07-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(max_length=64)),
                ('nombre', models.CharField(max_length=64)),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(max_length=64)),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
        ('myapp1', '0002_salesorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='product',
            field=models.ManyToManyField(to='myapp2.product'),
        ),
    ]

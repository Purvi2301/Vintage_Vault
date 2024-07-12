# Generated by Django 5.0.7 on 2024-07-11 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0006_itemcategory_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.CharField(max_length=255)),
                ('order_status', models.CharField(max_length=255)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vault.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vault.user')),
            ],
        ),
    ]

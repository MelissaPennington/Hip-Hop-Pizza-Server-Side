# Generated by Django 4.1.3 on 2024-01-09 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('payment_type', models.CharField(max_length=50)),
                ('order_type', models.CharField(max_length=50)),
                ('tip_amount', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_open', models.BooleanField(blank=True, null=True)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.customer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(default='Sally Smith', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.user'),
        ),
    ]
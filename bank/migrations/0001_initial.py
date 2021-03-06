# Generated by Django 3.0.5 on 2020-04-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=500, unique=True)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Bank')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branch',
                'ordering': ('bank_name',),
            },
        ),
    ]

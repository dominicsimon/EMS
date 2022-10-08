# Generated by Django 4.1.2 on 2022-10-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('owner', models.PositiveBigIntegerField()),
                ('parent', models.PositiveBigIntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('progress', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('budget_labor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('budget_material', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('budget_money', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('spent_labor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('spent_material', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('spent_money', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]

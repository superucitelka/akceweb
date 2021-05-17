# Generated by Django 3.2.3 on 2021-05-17 21:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200, verbose_name='Název akce')),
                ('datum', models.DateField(blank=True, help_text='Zadejte datum ve formátu: <em>YYYY-MM-DD</em>.', null=True, verbose_name='Datum konání akce')),
                ('popis', models.TextField(blank=True, null=True, verbose_name='Podrobnější popis akce')),
                ('kategorie', models.CharField(blank=True, choices=[('divadlo', 'Divadlo'), ('hudba', 'Hudba'), ('kino', 'Kino'), ('výstava', 'Výstava')], default='hudba', help_text='Vyberte kategorii akce', max_length=10, verbose_name='Kategorie akce')),
                ('hodnoceni', models.FloatField(default=5.0, help_text='Zadejte hodnocení v rozsahu (range 1.0 - 5.0)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Hodnocení')),
            ],
            options={
                'ordering': ['-datum', 'nazev'],
            },
        ),
    ]

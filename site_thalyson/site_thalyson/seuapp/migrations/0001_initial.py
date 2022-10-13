# Generated by Django 4.1.1 on 2022-09-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=256)),
                ('nascimento', models.DateField()),
                ('tel', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranked', '0003_rename_operator_armor_operator_operator_difficulty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=20)),
            ],
        ),
    ]

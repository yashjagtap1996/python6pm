# Generated by Django 4.1 on 2022-09-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('address', models.TextField(max_length=150)),
            ],
        ),
    ]

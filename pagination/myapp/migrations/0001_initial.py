# Generated by Django 4.0.4 on 2022-04-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('standard', models.CharField(blank=True, max_length=30)),
                ('contact_no', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-19 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]

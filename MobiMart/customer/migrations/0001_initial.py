# Generated by Django 3.1.4 on 2020-12-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compName', models.CharField(max_length=30)),
                ('mobName', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
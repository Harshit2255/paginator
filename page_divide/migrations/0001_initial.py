# Generated by Django 3.1 on 2020-09-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=500)),
                ('Post_Time', models.DateTimeField()),
            ],
        ),
    ]

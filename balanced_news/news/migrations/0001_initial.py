# Generated by Django 3.1.3 on 2020-12-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaning', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('img', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
    ]
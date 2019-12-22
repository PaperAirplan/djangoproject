# Generated by Django 3.0 on 2019-12-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('position', models.AutoField(primary_key=True, serialize=False)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_eng', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('publication_date', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]

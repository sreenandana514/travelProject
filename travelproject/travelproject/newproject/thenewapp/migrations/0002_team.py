# Generated by Django 4.2.7 on 2023-11-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thenewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pic')),
                ('des', models.TextField()),
            ],
        ),
    ]

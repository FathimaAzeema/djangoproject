# Generated by Django 3.2.9 on 2021-12-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211204_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
    ]

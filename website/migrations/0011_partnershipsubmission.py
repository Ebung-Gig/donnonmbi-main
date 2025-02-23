# Generated by Django 5.1.3 on 2024-11-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('organisation', models.CharField(blank=True, max_length=100)),
                ('partnership_category', models.CharField(choices=[('Resource Partner', 'Resource Partner'), ('Network Partner', 'Network Partner'), ('Learning Partner', 'Learning Partner')], max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]

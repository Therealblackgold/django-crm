# Generated by Django 3.2.9 on 2021-12-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact_person_1', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number_1', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_person_2', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number_2', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_person_3', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number_3', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_person_4', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number_4', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_person_5', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number_5', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('services', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

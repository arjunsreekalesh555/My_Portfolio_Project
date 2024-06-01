# Generated by Django 4.2.11 on 2024-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, null=True)),
                ('Date_of_birth', models.DateField(null=True)),
                ('Address', models.CharField(max_length=500, null=True)),
                ('Phone', models.CharField(max_length=11, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Degree', models.CharField(max_length=450, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Skills', models.CharField(max_length=500, null=True)),
                ('Freelance', models.BooleanField(default=True)),
                ('Image', models.ImageField(upload_to='bio')),
            ],
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, null=True)),
                ('Description', models.CharField(max_length=250, null=True)),
                ('Image', models.ImageField(upload_to='certificates')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, null=True)),
                ('Description', models.CharField(max_length=250, null=True)),
                ('Image', models.ImageField(upload_to='projects')),
            ],
        ),
    ]
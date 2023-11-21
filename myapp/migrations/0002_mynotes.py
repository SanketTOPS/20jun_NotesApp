# Generated by Django 4.2.5 on 2023-10-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='MyFiles')),
                ('comments', models.TextField()),
            ],
        ),
    ]

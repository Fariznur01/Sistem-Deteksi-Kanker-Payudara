# Generated by Django 3.2.9 on 2021-11-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(upload_to='files/excels/')),
                ('upload', models.DateField(null=True)),
                ('keterangan', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=10)),
                ('nis', models.IntegerField()),
            ],
        ),
    ]

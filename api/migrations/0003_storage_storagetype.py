# Generated by Django 3.0 on 2022-09-02 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_experiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('storage_temp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_full', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=50)),
                ('storage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_type_id', to='api.StorageType')),
            ],
        ),
    ]

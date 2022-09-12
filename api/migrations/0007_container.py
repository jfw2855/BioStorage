# Generated by Django 3.0 on 2022-09-11 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('is_full', models.BooleanField(default=False)),
                ('total_space', models.IntegerField()),
                ('space_available', models.IntegerField()),
                ('storage_location', models.CharField(max_length=50)),
                ('storage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_id', to='api.Storage')),
            ],
        ),
    ]
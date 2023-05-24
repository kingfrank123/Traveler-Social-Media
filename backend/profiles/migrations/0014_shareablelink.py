# Generated by Django 3.2.7 on 2021-10-17 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_savedlocation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareableLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=100)),
                ('origin_list', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.locationlist')),
            ],
        ),
    ]
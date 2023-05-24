# Generated by Django 3.2.9 on 2021-12-05 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='comment',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forums.post'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.12 on 2023-02-27 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.level'),
        ),
    ]

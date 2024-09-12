# Generated by Django 5.1.1 on 2024-09-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundamental_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appvariety',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='appvariety',
            name='image',
            field=models.ImageField(upload_to='apps/'),
        ),
        migrations.AlterField(
            model_name='appvariety',
            name='type',
            field=models.CharField(choices=[('ag', 'agriculture'), ('so', 'social'), ('ec', 'eco')], max_length=2),
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211129_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='address',
            field=models.CharField(help_text='Please provide the address where donations should be sent.', max_length=200),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='school_url',
            field=models.URLField(blank=True, help_text='Please enter a complete URL including the https://'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='zipcode',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.URLField(help_text='Please enter a complete URL including the https://', max_length=300),
        ),
    ]

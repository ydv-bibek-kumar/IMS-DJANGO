# Generated by Django 5.0.6 on 2024-06-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Department',
            field=models.ManyToManyField(null=True, to='hello.department'),
        ),
    ]

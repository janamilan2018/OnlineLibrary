# Generated by Django 4.0.1 on 2022-02-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]

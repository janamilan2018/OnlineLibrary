# Generated by Django 4.0.1 on 2022-03-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_remove_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('pdf', models.FileField(upload_to='PDF_File')),
            ],
        ),
    ]

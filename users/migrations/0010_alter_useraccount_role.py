# Generated by Django 4.1 on 2022-09-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_studentaccount_section_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('STAFF', 'Staff'), ('GUEST', 'Guest')], default=None, max_length=50),
        ),
    ]

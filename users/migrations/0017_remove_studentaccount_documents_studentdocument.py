# Generated by Django 4.1.2 on 2022-10-19 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_teacheraccount_useracc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentaccount',
            name='documents',
        ),
        migrations.CreateModel(
            name='StudentDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.ImageField(blank=True, null=True, upload_to='upload/student/documents')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.studentaccount')),
            ],
        ),
    ]
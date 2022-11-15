# Generated by Django 4.1.2 on 2022-11-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_studentaccount_documents_studentdocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffaccount',
            name='fullname',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='fullname',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='useracc',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='teacheraccount',
            name='fullname',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

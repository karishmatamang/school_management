# Generated by Django 4.1 on 2022-09-16 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0003_alter_grademodel_grade'),
        ('users', '0009_remove_studentaccount_section_id_and_more'),
        ('course', '0002_coursemodel_credit_hour'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.section')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacheraccount')),
            ],
        ),
    ]

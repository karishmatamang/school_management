# Generated by Django 4.1 on 2022-09-21 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_studentaccount_section_id_and_more'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_student',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentaccount'),
        ),
        migrations.CreateModel(
            name='Attendance_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.attendancemodel')),
                ('staff_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.staffaccount')),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacheraccount')),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-02-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_rename_act_no_student_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, default='Khiram', max_length=100, null=True, verbose_name='Address'),
        ),
    ]

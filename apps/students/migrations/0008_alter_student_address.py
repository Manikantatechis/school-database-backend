# Generated by Django 4.1.7 on 2023-02-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, default='Kasnard-Khiram', max_length=100, null=True, verbose_name='Address'),
        ),
    ]

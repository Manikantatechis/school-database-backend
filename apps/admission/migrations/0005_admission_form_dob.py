# Generated by Django 4.1.7 on 2023-02-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_rename_act_no_admission_form_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission_form',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]

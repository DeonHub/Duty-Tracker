# Generated by Django 4.1 on 2022-08-27 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssignedDutyActivities',
            new_name='MemberAssignedDutyActivities',
        ),
        migrations.RenameModel(
            old_name='ExtraWorkReport',
            new_name='MemberExtraWorkReport',
        ),
    ]

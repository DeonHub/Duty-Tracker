# Generated by Django 4.1 on 2022-08-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedDutyActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100, null=True)),
                ('member_category', models.CharField(max_length=100, null=True)),
                ('group', models.CharField(max_length=100, null=True)),
                ('subgroup', models.CharField(max_length=100, null=True)),
                ('member', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='file-uploads/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('duty_subject', models.CharField(max_length=100, null=True)),
                ('new_subject', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraWorkReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100, null=True)),
                ('member_category', models.CharField(max_length=100, null=True)),
                ('group', models.CharField(max_length=100, null=True)),
                ('subgroup', models.CharField(max_length=100, null=True)),
                ('member', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='file-uploads/')),
                ('overtime_message', models.CharField(max_length=500, null=True)),
                ('overtime_file', models.FileField(blank=True, default='', null=True, upload_to='file-uploads/')),
                ('percentage_done', models.IntegerField(null=True)),
                ('duty_subject', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedDutyReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100, null=True)),
                ('member_category', models.CharField(max_length=100, null=True)),
                ('group', models.CharField(max_length=100, null=True)),
                ('subgroup', models.CharField(max_length=100, null=True)),
                ('member', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='file-uploads/')),
                ('overtime_message', models.CharField(max_length=500, null=True)),
                ('overtime_file', models.FileField(blank=True, default='', null=True, upload_to='file-uploads/')),
                ('duty_subject', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0006_name_token_alter_recieveddutyreports_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='overtime_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='file-uploads/'),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='overtime_message',
            field=models.CharField(default='No message', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='overtime_subject',
            field=models.CharField(default='No subject', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='percentage_done',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='reassigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='reassigned_from',
            field=models.CharField(default='No one', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='reassigned_to',
            field=models.CharField(default='No one', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='remarks',
            field=models.CharField(default='No remarks', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='report_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='file-uploads/'),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='report_message',
            field=models.CharField(default='No message', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='self_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='work_status',
            field=models.CharField(default='Undone', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='assigneddutyactivities',
            name='rating',
            field=models.CharField(default='Unrated', max_length=500, null=True),
        ),
    ]
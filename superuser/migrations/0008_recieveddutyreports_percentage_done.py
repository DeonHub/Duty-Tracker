# Generated by Django 4.1 on 2022-09-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0007_assigneddutyactivities_assigned_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recieveddutyreports',
            name='percentage_done',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
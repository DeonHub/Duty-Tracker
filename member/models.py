from django.db import models

# Create your models here.
class MemberAssignedDutyActivities(models.Model):
    branch = models.CharField(max_length= 100, null=True)
    member_category = models.CharField(max_length= 100, null=True)
    group = models.CharField(max_length= 100, null=True)
    subgroup = models.CharField(max_length= 100, null=True)
    member = models.CharField(max_length= 100, null=True)
    message = models.CharField(max_length= 500, null=True)
    file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    duty_subject = models.CharField(max_length= 100, null=True)
    new_subject = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'

class SubmittedDutyReports(models.Model):
    branch = models.CharField(max_length= 100, null=True)
    member_category = models.CharField(max_length= 100, null=True)
    group = models.CharField(max_length= 100, null=True)
    subgroup = models.CharField(max_length= 100, null=True)
    member = models.CharField(max_length= 100, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    message = models.CharField(max_length= 500, null=True)
    file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    overtime_message = models.CharField(max_length= 500, null=True)
    overtime_file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    duty_subject = models.CharField(max_length= 100, null=True)
    work_status = models.CharField(max_length= 100, null=True)
    rating = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'


class MemberExtraWorkReport(models.Model):
    branch = models.CharField(max_length= 100, null=True)
    member_category = models.CharField(max_length= 100, null=True)
    group = models.CharField(max_length= 100, null=True)
    subgroup = models.CharField(max_length= 100, null=True)
    member = models.CharField(max_length= 100, null=True)
    message = models.CharField(max_length= 500, null=True)
    file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    overtime_message = models.CharField(max_length= 500, null=True)
    overtime_file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    percentage_done = models.IntegerField(null=True)
    duty_subject = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'

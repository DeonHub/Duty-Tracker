from django.db import models

# Create your models here.
class DutySubject(models.Model):
    duty_subject = models.CharField(max_length=500,  null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.duty_subject

class Member(models.Model):
    member = models.CharField(max_length=200, null=True)   
    member_category = models.CharField(max_length=200, null=True)   
    date_created = models.DateField(auto_now_add=True) 
   
    def __str__(self):
        return f'{self.member}'


class DutyEarnings(models.Model):
    branch = models.CharField(max_length= 100, null=True)
    member_category = models.CharField(max_length= 100, null=True)
    group = models.CharField(max_length= 100, null=True)
    subgroup = models.CharField(max_length= 100, null=True)
    member = models.CharField(max_length= 100, null=True)
    duty_subject = models.CharField(max_length= 100, null=True)
    daily_work_earning = models.IntegerField(null=True)
    overtime_earning = models.IntegerField(null=True)
    currency = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.daily_work_earning}, {self.duty_subject}'



class AssignedDutyActivities(models.Model):
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

    report_status = models.CharField(max_length= 100, null=True, default="Not submitted")

    report_message = models.CharField(max_length= 500, null=True, default="No message")
    report_file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    overtime_message = models.CharField(max_length= 500, null=True, default="No message")
    overtime_subject = models.CharField(max_length= 500, null=True, default="No subject")
    overtime_file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    percentage_done = models.IntegerField(null=True, default=0)

    work_status = models.CharField(max_length= 500, null=True, default="Undone")
    
    rating = models.CharField(max_length= 500, null=True, default="Unrated")
    remarks = models.CharField(max_length= 500, null=True, default="No remarks")

    extra = models.BooleanField(default=False)

    assigned = models.BooleanField(default=False)
    self_assigned = models.BooleanField(default=False)
    reassigned = models.BooleanField(default=False)

    reassigned_to = models.CharField(max_length= 500, null=True, default="No one")
    reassigned_from = models.CharField(max_length= 500, null=True, default="No one")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'




class RecievedDutyReports(models.Model):
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
    overtime_subject = models.CharField(max_length= 500, null=True)
    overtime_file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    duty_subject = models.CharField(max_length= 100, null=True)
    new_subject = models.CharField(max_length= 100, null=True)
    work_status = models.CharField(max_length= 500, null=True)
    rating = models.CharField(max_length= 500, null=True, default="Unrated")
    extra = models.BooleanField(default=False)
    percentage_done = models.IntegerField(null=True, default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'


class ExtraWorkReport(models.Model):
    branch = models.CharField(max_length= 100, null=True)
    member_category = models.CharField(max_length= 100, null=True)
    group = models.CharField(max_length= 100, null=True)
    subgroup = models.CharField(max_length= 100, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    member = models.CharField(max_length= 100, null=True)
    message = models.CharField(max_length= 500, null=True)
    file = models.FileField(blank=True, null=True, upload_to='file-uploads/', default='')
    percentage_done = models.IntegerField(null=True)
    extra = models.BooleanField(default=True)
    duty_subject = models.CharField(max_length= 100, null=True)
    work_status = models.CharField(max_length= 500, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member}, {self.duty_subject}'


class Token(models.Model):
    token = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return self.token


class Name(models.Model):
    name = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return self.name


class ActivityLog(models.Model):
    user = models.CharField(max_length= 100, null=True)
    action = models.CharField(max_length= 100, null=True)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.user} {self.action}"
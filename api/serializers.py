from django.forms import ValidationError
from rest_framework import serializers
from .models import *
from superuser.models import *


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    role = serializers.CharField()

    def validate_email(self, value):
        if len(value) < 5:
            raise ValidationError("No Jokes please")
        return value 
    
    def validate_password(self, value):
        if value == "":
            raise ValidationError("No Jokes please")
        return value 



class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, value):
        if value == "":
            raise ValidationError("This field is required")
        return value        



class CommentSerializer(serializers.Serializer):
    rating = serializers.CharField(required=False)
    remarks = serializers.CharField(required=False)

    def get_validation_exclusions(self):
        exclusions = super(CommentSerializer, self).get_validation_exclusions()
        return exclusions + ['rating']


class DutyReportSerializer(serializers.ModelSerializer):

    class Meta():
        model = RecievedDutyReports
        # fields = '__all__'
        fields = ('message', 'file', 'overtime_file', 'overtime_subject', 'overtime_message', 'work_status', 'percentage_done')


    def validate_message(self, value):
        if value == "" or value == None:
            raise ValidationError("Message cant be empty")
        return value   

    # def validate(self, data):
    #     if len(data["name"]) < 5 or len(data["alias"]) < 5:
    #         raise ValidationError("Name should be more than 5")  
    #     return data     



class ExtraWorkReportSerializer(serializers.Serializer):

    duty_subject = serializers.CharField()
    message = serializers.CharField()
    file = serializers.FileField(required=False)
    percentage_done = serializers.IntegerField()
    work_status = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(ExtraWorkReportSerializer, self).get_validation_exclusions()
        return exclusions + ['file']


    def validate_message(self, value):
        if value == "":
            raise ValidationError("Message")
        return value   




# Superuser serializers

# All assigned duties
class AssignedDutiesSerializer(serializers.ModelSerializer):

    class Meta():
        model = AssignedDutyActivities
        fields = '__all__'
        # fields = ('message', 'file', 'overtime_file', 'overtime_message', 'work_status')


class ReceivedDutiesSerializer(serializers.ModelSerializer):

    class Meta():
        model = RecievedDutyReports
        fields = '__all__'
        # fields = ('message', 'file', 'overtime_file', 'overtime_message', 'work_status')



class ExtraReportSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = ExtraWorkReport
        fields = '__all__'
        
        # fields = ('message', 'file', 'overtime_file', 'overtime_message', 'work_status')



# Member serializers

# # All assigned duties
# class MemberAssignedDutiesSerializer(serializers.ModelSerializer):

#     class Meta():
#         model = MemberAssignedDutyActivities
#         fields = '__all__'
#         # fields = ('message', 'file', 'overtime_file', 'overtime_message', 'work_status')


# class MemberReceivedDutiesSerializer(serializers.ModelSerializer):

#     class Meta():
#         model = SubmittedDutyReports
#         fields = '__all__'
#         # fields = ('message', 'file', 'overtime_file', 'overtime_message', 'work_status')



# Assign duty serializer

class AssignDutySerializer(serializers.Serializer):


        class Meta():
            model = AssignedDutyActivities
            # fields = '__all__'
            fields = (
                "branch",
                "member_category",
                "group",
                "subgroup",
                "member",
                "message",
                "file",
                "start_date",
                "end_date",
                "start_time",
                "end_time",
                "duty_subject",
                "new_subject",
                "assigned",
                "self_assigned",
                "reassigned",
                "reassigned_to",
                "reassigned_from",

                )


class SubjectsSerializer(serializers.Serializer):

    class Meta():
        model = DutySubject
        fields = "__all__"
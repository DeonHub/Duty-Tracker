import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from superuser.models import *
from member.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from itertools import chain
import requests
import json

# Create your views here.
member = "Lord Asante"
# admin = 'admin'

# print(AssignedDutyActivities.objects.filter(member=member))        
class Login(APIView):

    def post(self, request, *args):

        today = datetime.date.today()
        year = datetime.datetime.now().year
        year = str(year) + "0000"

        members = LoginSerializer(data=request.data)

        if members.is_valid():
            email = members.data['email']
            password = members.data['password']
            role = members.data['role']

            if role == "admin" or role == "Admin":
    
                items = []
                url = "https://db-api-v2.akwaabasoftware.com/clients/login"
                payload = json.dumps({"phone_email": email, "password": password, "checkDeviceInfo": False})
                headers = {'Content-Type': 'application/json', 'Cookie': 'csrftoken=4QyiPkebOBXrv202ShwWThaE1arBMWdnFnzdsgyMffO6wvun5PpU6RJBTLRIdYDo; sessionid=rsg9h5tu73jyo3hl2hvgfm0qcd7xmf92'}
                key = requests.request("POST", url, headers=headers, data=payload).json()
                user = requests.request("POST", url, headers=headers, data=payload).json()

                for item in key.keys():
                    items.append(item)

                if "non_field_errors" in items:  
                    error = {
                        "success": False,
                        "message": "Incorrect email or password",
                    }

                    return Response(error, status=status.HTTP_400_BAD_REQUEST)   
                else:
                    token = key['token']
                    
                    response = requests.request("POST", url, headers=headers, data=payload).json()['user']

                    try:
                        firstname = response['firstname'] 
                        surname = response['surname']

                    except:
                        pass    

                    # if middlename != '':
                    #     name = f'{firstname} {middlename} {surname}'
                    # else: 

                    name = f'{firstname} {surname}' 

                    tokenise = Token.objects.create(token=token)  
                    tokenise.save()  

                    # for member name
                    new_name = Name.objects.all()
                    if len(new_name) > 0:
                        new_name.delete()

                    normalise = Name.objects.create(name=name)  
                    normalise.save()      

                    nameken = Nameken.objects.create(
                        name=name,
                        token=token,
                        role=role
                    )
                    nameken.expiry_date =  today + datetime.timedelta(days=(int(15)))
                    nameken.save() 

                    ash = Token.objects.all().first()  

                    data = {
                        "success": True,
                        "duty_token": ash.token,
                        # "name": name,
                        # "total_assigned": "{:,}".format(total_assigned),
                        # "total_paid": "{:,}".format(total_paid)
                    }

                    return Response(data, status=status.HTTP_200_OK)

            elif role=="member" or role=="client" or role=="student":         

                items = []
                url = "https://db-api-v2.akwaabasoftware.com/members/login"
                payload = json.dumps({"phone_email": email, "password": password, "checkDeviceInfo": False})
                headers = {'Content-Type': 'application/json', 'Cookie': 'csrftoken=4QyiPkebOBXrv202ShwWThaE1arBMWdnFnzdsgyMffO6wvun5PpU6RJBTLRIdYDo; sessionid=rsg9h5tu73jyo3hl2hvgfm0qcd7xmf92'}
                key = requests.request("POST", url, headers=headers, data=payload).json()

                for item in key.keys():
                    items.append(item)

                if "non_field_errors" in items:  

                    error = {
                        "success": False,
                        "message": "Incorrect email or password",
                    }

                    return Response(error, status=status.HTTP_400_BAD_REQUEST)

                else: 
                    user = requests.request("POST", url, headers=headers, data=payload).json()['user']
                    token = key['token']

                    new_token = Token.objects.all()
                    if len(new_token) > 0:
                        new_token.delete()

                    tokenise = Token.objects.create(token=token)  
                    tokenise.save()  

                    member_id = user['id']

                    # Getting the client
                    url = f"https://db-api-v2.akwaabasoftware.com/members/user/{member_id}"
                    payload = json.dumps({ "phone_email":email, "password": password, "checkDeviceInfo": False })

                    headers = {'Authorization': f'Token {token}', 'Content-Type': 'application/json', 'Cookie': 'csrftoken=PmuB7mZ3fXkrs8rg8AG9hT4lirE2iMuHa1ekEEty3Z7pCWZBqIXmqD1b0WXZQzvw; sessionid=ruu6ibfixx18a2o91hvw86jgjrgrg144'}

                    response = requests.request("GET", url, headers=headers, data=payload).json()['data']


                    firstname = response['firstname'] 
                    middlename = response['middlename']
                    surname = response['surname']

                    if middlename != '':
                        name = f'{firstname} {middlename} {surname}'
                    else: 
                        name = f'{firstname} {surname}'  


                    # for member name
                    new_name = Name.objects.all()
                    if len(new_name) > 0:
                        new_name.delete()

                    normalise = Name.objects.create(name=name)  
                    normalise.save()      

                    nameken = Nameken.objects.create(
                        name=name,
                        token=token,
                        role=role
                    )
                    
                    nameken.expiry_date =  today + datetime.timedelta(days=(int(15)))
                    nameken.save() 

                    ash = Token.objects.all().first()

                    # Getting the total assigned amount

                    # total_assigned = 0
                    # try:
                    #     duties = AssignPaymentDuration.objects.filter(member=name)

                    #     for x in duties:
                    #         if x.total_invoice == None:
                    #             pass
                    #         else:
                    #             total_assigned += int(x.total_invoice)
                    # except:
                    #     print("Member does not exist")
                    #     pass       


                    # # Getting total paid
                    # total_paid = 0
                    # try:
                    #     duties = MakePayment.objects.filter(member=member, donation_name=None)
                    #     # print(duties)

                    #     for x in duties:
                    #         if x.amount_paid == None:
                    #             pass
                    #         else:
                    #             # print(x.total_invoice)
                    #             total_paid += int(x.amount_paid)
                    # except:
                    #     print("Member does not exist")
                    #     pass  

                    data = {
                        "success": True,
                        "duty_token": ash.token,
                        # "name": name,
                        # "total_assigned": "{:,}".format(total_assigned),
                        # "total_paid": "{:,}".format(total_paid)
                    }

                    return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                        "success": False,
                        "message": "Enter a valid role",
                    }
                return Response(data, status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(members.errors, status=status.HTTP_400_BAD_REQUEST)  





class AssignDuty(APIView):

    def post(self, request, *args):
    
        new_duty = AssignDutySerializer(data=request.data)

        if new_duty.is_valid():
            branch = new_duty.data['branch']
            member_category = new_duty.data['member_category']
            group = new_duty.data['group']
            subgroup = new_duty.data['subgroup']
            member = new_duty.data['member']
            message = new_duty.data['message']
            file = new_duty.data['file']
            start_date = new_duty.data['start_date']
            end_date = new_duty.data['end_date']
            start_time = new_duty.data['start_time']
            end_time = new_duty.data['end_time']
            duty_subject = new_duty.data['duty_subject']
            new_subject = new_duty.data['new_subject']
            self_assigned = new_duty.data['self_assigned']
            reassigned = new_duty.data['reassigned']
            assigned = new_duty.data['assigned']
            reassigned_to = new_duty.data['reassigned_to']
            reassigned_from = new_duty.data['reassigned_from']
            
            
            assigned_duty = AssignedDutyActivities.objects.create(
                branch=branch,
                member_category=member_category,
                group=group,
                subgroup=subgroup,
                member=member,
                message=message,
                file=file,
                start_date=start_date,
                end_date=end_date,
                start_time=start_time,
                end_time=end_time,
                duty_subject=duty_subject,
                new_subject=new_subject,

                assigned=assigned,
                self_assigned=self_assigned,
                reassigned=reassigned,
                reassigned_to=reassigned_to,
                reassigned_from=reassigned_from,
 
            )
            
            assigned_duty.save()

            return Response(new_duty.data, status=status.HTTP_200_OK)
        else:
            return Response(new_duty.errors, status=status.HTTP_400_BAD_REQUEST)  





class GetSubjects(APIView):

    def get(self, request):
        subjects = DutySubject.objects.all()
        subject = SubjectsSerializer(subjects)
        return Response(subject.data)




class AddComment(APIView):

    def get_duty_by_pk(self, pk):

        try:
            return AssignedDutyActivities.objects.get(pk=pk)
        except:
            return Response({
                "error": "Duty does not exist"
            }, status=status.HTTP_404_NOT_FOUND)   

    
    def post(self, request, pk):

        # assigned_duty = self.get_duty_by_pk(pk)
        assigned_duty = AssignedDutyActivities.objects.get(pk=pk)
        report = CommentSerializer(data=request.data)

        if report.is_valid():
            try:
                rating = report.data['rating']
            except:    
                rating = ""
            try:
                remarks = report.data['remarks'] 
            except:
                remarks = ""


            if rating != "":
                assigned_duty.rating = rating
                assigned_duty.save()

            if remarks != "":
                assigned_duty.remarks = remarks
                assigned_duty.save()


            return Response(report.data)
        else:
            return Response(report.errors, status=status.HTTP_400_BAD_REQUEST)    



class AddReport(APIView):

    def get_duty_by_pk(self, pk):

        try:
            return AssignedDutyActivities.objects.get(pk=pk)
        except:
            return Response({
                "error": "Duty does not exist"
            }, status=status.HTTP_404_NOT_FOUND)   


    # def get(self, request, pk):
    #     # duties = self.get_duty_by_pk(pk)
    #     duties = AssignedDutyActivities.objects.get(pk=pk)
    #     duty = AssignedDutiesSerializer(duties)
    #     return Response(duty.data)

    
    def post(self, request, pk):

        try:
            if len(Name.objects.all()) > 0:
                member = Name.objects.all().first().name
            else:
                member = ""
        except:
            member = ""

        assigned_duty = AssignedDutyActivities.objects.get(pk=pk)
        report = DutyReportSerializer(data=request.data)

        if report.is_valid():
            branch = assigned_duty.branch
            member_category = assigned_duty.member_category
            group = assigned_duty.group
            subgroup = assigned_duty.subgroup
            member = assigned_duty.member
            start_date = assigned_duty.start_date
            end_date = assigned_duty.end_date
            start_time = assigned_duty.start_time
            end_time = assigned_duty.end_time
            duty_subject = assigned_duty.duty_subject
            new_subject = assigned_duty.new_subject
            message = report.data['message']
            file = report.data['file']
            overtime_message = report.data['overtime_message']
            overtime_subject = report.data['overtime_subject']
            overtime_file = report.data['overtime_file']
            work_status = report.data['work_status']
            percentage_done = report.data['percentage_done']

            duty_report = RecievedDutyReports(
                branch=branch,
                member_category=member_category,
                group=group,
                subgroup=subgroup,
                member=member,
                start_date=start_date,
                end_date=end_date,
                start_time=start_time,
                end_time=end_time,
                duty_subject=duty_subject,
                new_subject=new_subject,
                message=message,
                file=file,
                overtime_subject=overtime_subject,
                overtime_message=overtime_message,
                overtime_file=overtime_file,
                work_status=work_status,
                percentage_done=percentage_done
            )
            duty_report.save()

            assigned_duty.report_status = "Submitted"
            assigned_duty.report_message = report.data['message']
            assigned_duty.report_file = report.data['file']
            assigned_duty.overtime_message = report.data['overtime_message']
            assigned_duty.overtime_subject = report.data['overtime_subject']
            assigned_duty.overtime_file = report.data['overtime_file']
            assigned_duty.work_status = report.data['work_status']
            assigned_duty.percentage_done = report.data['percentage_done']

            assigned_duty.save()

            return Response(report.data)
        else:
            return Response(report.errors, status=status.HTTP_400_BAD_REQUEST)    




class AddExtraWorkReport(APIView):
    
    def post(self, request):
        try:
            if len(Name.objects.all()) > 0:
                member = Name.objects.all().first().name
            else:
                member = ""
        except:
            member = ""

        report = ExtraWorkReportSerializer(data=request.data)

        if report.is_valid():
            message = report.data['message']
            start_time = report.data['start_time']
            end_time = report.data['end_time']
            file = report.data['file']
            percentage_done = report.data['percentage_done']
            work_status = report.data['work_status']
            duty_subject = report.data['duty_subject']

            duty_report = ExtraWorkReport(
                message=message,
                file=file,
                start_time=start_time,
                end_time=end_time,
                percentage_done=percentage_done,
                duty_subject=duty_subject,
                work_status=work_status,
                member=member
            )
            duty_report.save()

            return Response(report.data)
        else:
            return Response(report.errors, status=status.HTTP_400_BAD_REQUEST)    



# class AssignedDuty(APIView):

#     def get_duty_by_pk(self, pk):
#         try:
#             return Hero.objects.get(pk=pk)
#         except:
#             return Response({
#                 "error": "Duty does not exist"
#             }, status=status.HTTP_400_NOT_FOUND)   


#     def get(self, request, pk):
#         heroes = self.get_hero_by_pk(pk)
#         hero = HeroSerializer(heroes)
#         return Response(hero.data)


#     def put(self, request, pk):
#         heroes = self.get_hero_by_pk(pk)
#         hero = HeroSerializer(heroes, data=request.data)
#         if hero.is_valid():
#             hero.save()
#             return Response(hero.data)
#         else:
#             return Response(hero.errors, status=status.HTTP_400_BAD_REQUEST) 

#     def delete(self, request, pk):
#         heroes = self.get_hero_by_pk(pk)
#         heroes.delete()  
#         return Response(status=status.HTTP_204_NO_CONTENT) 
    



# Superuser apis

# Getting all assigned duties
class ViewAssignedTasks(APIView):

    def get(self, request):
        all_heroes = AssignedDutyActivities.objects.all()
        heroes = AssignedDutiesSerializer(all_heroes, many=True)
        
        return Response(heroes.data)


class ViewSubmittedTasks(APIView):

    def get(self, request):
        all_heroes = RecievedDutyReports.objects.all()
        all_extras = ExtraWorkReport.objects.all()
        all_works = list(chain(all_heroes, all_extras))
        heroes = ReceivedDutiesSerializer(all_works, many=True)
        
        return Response(heroes.data)
            


class ExtraWorkReport(APIView):
    
    def get(self, request):
        all_heroes = ExtraWorkReport.objects.all()
        heroes = ExtraReportSerializer(all_heroes, many=True)
        
        return Response(heroes.data)



# client apis
# Getting all assigned duties
class MemberAssignedDuties(APIView):

    def post(self, request):
        
        valid_token = TokenSerializer(data=request.data)
        today = datetime.date.today()


        if valid_token.is_valid():

            token = valid_token.data['token']

            try:
                passed_token = Nameken.objects.get(token=token)

                if today < passed_token.expiry_date:

                    member = passed_token.name

                    all_duties = AssignedDutyActivities.objects.filter(member=member)
                    duties = AssignedDutiesSerializer(all_duties, many=True)
            
                    return Response(duties.data, status=status.HTTP_200_OK)

                else:
                    passed_token.delete()

                    expired = {
                        "success": False,
                        "message": "Expired token"
                    }

                    return Response(expired, status=status.HTTP_400_BAD_REQUEST)

            except:
                error = {
                    "success": False,
                    "message": "Invalid token"
                    }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)       
        else:
            return Response(valid_token.errors, status=status.HTTP_400_BAD_REQUEST) 






class MemberSubmittedTasks(APIView):

    def post(self, request):

        try:
            if len(Name.objects.all()) > 0:
                member = Name.objects.all().first().name
            else:
                member = ""
        except:
            member = ""


        old_token = Token.objects.all().first()
        valid_token = TokenSerializer(data=request.data)

        if valid_token.is_valid():
            token = valid_token.data['token']

            if token == old_token.token:
        
                all_heroes = RecievedDutyReports.objects.all(member=member)
                all_extras = ExtraWorkReport.objects.all(member=member)
                all_works = list(chain(all_heroes, all_extras))
                heroes = ReceivedDutiesSerializer(all_works, many=True)
                
                return Response(heroes.data, status=status.HTTP_200_OK)
            else:
                error = {
                    "success": False,
                    "message": "Invalid token"
                    }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response(valid_token.errors, status=status.HTTP_400_BAD_REQUEST)  
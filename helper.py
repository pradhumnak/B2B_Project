import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','B2B_Project.settings')
import django
django.setup()
from B2B_App.models import IdentifierTable, InquiryTable
import datetime


def GetLastReqIdfromDb():
    latestId = IdentifierTable.objects.latest('reqid')
    print(latestId)
    return str(latestId)

def GetEmailIdfromDb(em):
    emailid = (InquiryTable.objects.filter(email=em))
    return emailid
    


def GenerateNewReqId():
    latestId = GetLastReqIdfromDb()
    latestId = latestId.partition('REQ')
    num = int(latestId[2])
    num= num +1
    latestId = str(str(latestId[1])+str(num))
    print(type(latestId))
    return latestId


def InsertDataInDb(arrayLis, rid):
    print('Request Id : {}'.format(rid))
    print('First Name: {}'.format(arrayLis[0]))
    print('Last Name: {}'.format(arrayLis[1]))
    print('Email: {}'.format(arrayLis[2]))
    print('Country Code: {}'.format(arrayLis[3]))
    print('Mobile Number: {}'.format(arrayLis[4]))
    print('Message: {}'.format(arrayLis[5]))
    print('Date: {}'.format(datetime.datetime.now()))

    requestId = IdentifierTable.objects.get_or_create(reqid=rid)[0]
    requestId.save()
    instTab = InquiryTable.objects.get_or_create(first_name=arrayLis[0], last_name=arrayLis[1],email=arrayLis[2],ReqId=requestId, CountryCode=arrayLis[3],mobileNo=arrayLis[4],message=arrayLis[5],date=datetime.datetime.now())[0]
    instTab.save()
    print('Values inserted in Database')
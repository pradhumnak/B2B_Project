from django.shortcuts import render
from django.http import HttpResponse
import helper



# Create your views here.

def index(request):
    dict = {'success_msg':'Login Success'}
    return render(request,'B2B_App/index.html',context=dict)

def fdrpage(request):
    
    if request.method == 'POST':
        form = request.POST
        qset = helper.GetEmailIdfromDb(form['email'])
        print(qset)
        if qset.exists():
            result ='Congratulations, You are already regestered with us !'
        else:
            reqid = helper.GenerateNewReqId()
            feedList = [str(form['f_name']),str(form['l_name']), str(form['email']),int(form['c_code']),int(form['mob_num']),str(form['message'])]
            helper.InsertDataInDb(feedList, reqid) 
            result = 'Conratulations , your registration was successful . Your request id is : {}'.format(reqid)
        
    dict = {'congrats':result}
    return render(request,'B2B_App/fdrpage.html',context=dict)

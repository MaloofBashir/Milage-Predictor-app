from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import joblib
import pandas as pd
import sklearn

modelReload=joblib.load('/Users/maloofbashir/projects/django/milage-ml-app/Model/NewMPGmodel.pkl')



# Create your views here.



def index(request):
    temp={}
    temp["cylinders"]=1
    temp['displacement']=2
    temp['horsepower']=3
    temp['weight']=4
    temp['acceleration']=5
    temp['model year']=6
    temp['origin']=1
    testDtaa=pd.DataFrame({'x':temp}).transpose()
    scoreval=modelReload.predict(testDtaa)
    context={'my':"name is babu",'val':scoreval}

    return render(request,"index.html",context)

def predictMPG(request):
    
    temp={}
    if request.method=='POST':
        temp={}
        temp["cylinders"]=request.POST.get("cylinderVal")
        temp['displacement']=request.POST.get("dispVal")
        temp['horsepower']=request.POST.get("hrspwrVal")
        temp['weight']=request.POST.get("weightVal")
        temp['acceleration']=request.POST.get("accVal")
        temp['model_year']=request.POST.get("modVal")
        temp['origin']=request.POST.get("originVal")
        temp2=temp.copy()
        temp2['model year']=temp['model_year']
        print (temp.keys(),temp2.keys())
    testDtaa=pd.DataFrame({'x':temp2}).transpose()
    scoreval=modelReload.predict(testDtaa)[0]
    scoreval=round(scoreval,2)
    context={'scoreval':scoreval,'temp':temp}
    return render(request,'mpg.html',context)

    
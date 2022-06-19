from django.shortcuts import render
import os
# Create your views here.
pathdir =os.getcwd()
pathdir = pathdir.replace("\\", "/")
import pandas as pd
path = pathdir + '/graphApp/templates/graphApp/TransactionData.csv'
file = pd.read_csv(path)
date= file.iloc[:,1:2].values        
transact= file.iloc[:,2:5:2].values        
total= file.iloc[:,5:6].values        
length = len(date)

def index(request):
    params = {"date": date , 'length': length,'total': total}
    return render(request,'graphApp/index.html',params)
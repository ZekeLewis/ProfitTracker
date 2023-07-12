from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data
# Create your views here.


def hello(request):
    if (request.method == 'POST'):
        previous_data = Data.objects.all()
        previous_data.delete()
        file = request.FILES['file']
        df = pd.read_csv(file, sep=',')
        json_records = df.to_json(orient='records')
        data = []
        data = json.loads(json_records)
        for d in data:
            name = d['Product_Name']
            price = d['Price']
            sales = d['Sales']
            emp = d['Employee_Salary']
            tax = d['Tax']
            exp = d['Other_Expenses']
            expenses_monthly = emp+tax+exp
            income_monthly = sales - expenses_monthly
            dt = Data(name=name,price=price,sales=sales,emp=emp,tax=tax,exp=exp,expenses_monthly=expenses_monthly,income_monthly=income_monthly)
            dt.save()
        data_objects = Data.objects.all()
        context = {'data_objects': data_objects}
        return render(request, 'myapp/index.html', context)
    else:
        print('This is a get request')
    return render(request, 'myapp/index.html')
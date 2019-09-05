from django.shortcuts import render
from . import forms
import requests

def currency_view(request):
     form=forms.currencyform()
     if request.method=='POST':
         form=forms.currencyform(request.POST)
         if form.is_valid():

           amount=form.cleaned_data['amount']
           Homecurrency=form.cleaned_data['Homecurrency']
           Targetcurrency=form.cleaned_data['Targetcurrency']
           #print('Targetcurrency')

           response = requests.get('http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7')
           currencydata = response.json()

           x=currencydata['rates'][Homecurrency]
           y=currencydata['rates'][Targetcurrency]
           #rates=currencydata['rates'][Targetcurrency]
           currency=amount*(y/x)


          # rate={'currencydata':currencydata['rate']}
           #print(currencydata)
           return render(request, 'currencyapp/display.html',{'currency':currency,'Homecurrency':Homecurrency,'Targetcurrency':Targetcurrency,'amount':amount})

     return render(request,'currencyapp/currency.html',{'form':form})

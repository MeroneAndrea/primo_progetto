from django.shortcuts import render
import datetime
# Create your views here.
#L6
def esempio_if(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    dic = { 'var1' : 200,
    'var2' : 200,
    'var3' : 300 }
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render(request, "es_if.html", dic)

#L7
def esempio_ifelse(request):
    #https://www.decodejava.com/django-template-if-else-tag.htm
    dic = { 'var1' : 'admin',
    'var2' : 'admin',
    'var3' : 600 }
    return render(request, "es_ifelse.html", dic)

#L8
def esempio_elif(request):
    dic = { 'var1' : 100,
    'var2' : 100.0,
    'var3' : 100.50,
    'str1' : 'Hello',
    'str2' : 'hello',
    'str3' : "Hello",
    'list1': [1, datetime.date(2019,7,16), 'Make your life productive!'],
    'list2': [2, datetime.date(2019,7,16), 'Do not give up!']}
    return render(request, "es_ifelif.html", dic)

#L9
def esempio_for(request):
    #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "es_for.html", dic)
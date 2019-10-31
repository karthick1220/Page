#1
#http://127.0.0.1:8000/hello/
# from django.shortcuts import render
# import datetime
# 
# # Create your views here.
# def hello(request):
#    today = datetime.datetime.now().date()
#    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#    return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

#whole
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})
    
def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)
    
def viewArticles(request, year, month):
   test = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(test)
from django.shortcuts import render,redirect
from datetime import datetime,timedelta
from django.http.response import HttpResponse
def home(request):
    response= render(request, 'home.html')
    response.set_cookie('name','murad')
    # response.set_cookie('name','Sadia',max_age=10)
    response.set_cookie('name','Sadia',expires=datetime.utcnow()+timedelta(days=30))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    # print(request.name)
    return render(request, 'cookies.html',{'name':name})

def delete_cookies(request):
    response= render(request, 'cookies.html')
    response.delete_cookie('name')
    

def set_sessions(request):
    data ={
        'name' : 'murad',
        'age' : 23,
        'language' : 'Bangla'
    }
    # request.session['name'] = 'Murad'
    request.session.update(data)
    return render(request,'home.html')

def get_sessions(request):
    if 'name' in request.session:
       name = request.session.get('name','Guest')
    # print(request.name)
       return render(request, 'session.html',{'name':name})
    else:
        return HttpResponse('Your are fired,Login Again')

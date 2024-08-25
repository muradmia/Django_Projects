from django.shortcuts import render

# Create your views here.
def app(request):
    d = {'author' : 'Murad','age' : 20,'self'  : 'Tanvir','lst'  : [1,2,3],'hey'  :30,

    'courses' : [
        {
            'Id' : 1,
            'Name' : 'Py'
        },
        {
            'Id' : 2,
            'Name' : 'java'
        },
        {
            'Id' : 3,
            'Name' : 'DB'
        },
    ]}
    return render(request,'app.html',d)

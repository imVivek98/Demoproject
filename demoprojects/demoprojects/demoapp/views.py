
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def arithmetic(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    addn = x+y
    subn = x-y
    muln = x * y
    divn = x/y
    return render(request,'results.html',{'addition':addn,'subtraction':subn,'multiplication':muln,'division':divn})





#def about(request):
#    return HttpResponse("I,m the about page.")


#def contact(request):
#   return render(request,'contacts.html')


#def details(request):
#    return HttpResponse("Hello,I'm the details section")

#def thanks(request):
#    return render(request,'thanks.html')



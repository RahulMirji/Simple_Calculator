from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):
    c=''
    try:
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="Invalid Opr"
    return render(request,"calculator.html",{'c':c})

def evenodd(request):
    if request.method == "POST":
        n = eval(request.POST.get('num1'))
        if n % 2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
        return render(request, "evenodd.html", {'c': c})

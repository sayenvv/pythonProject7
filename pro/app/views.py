import random
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render

def home(request):
    return render(request,'home.html')
new= [0]

def dice(request):
    if request.method == "POST":
        if 'value' in request.POST:
            ans = random.randint(1, 6)
            new.append(ans)
            x=sum(new)

            if x % 7 == 0:
                new.clear()
                messages.error(request, "game over..!!,your score is zero")
            if x >= 100:
                messages.success(request, "congratulations,you got 100 points..")
            return render(request, 'dice.html', {"ans": ans,"x":x})
    return render(request,'dice.html')

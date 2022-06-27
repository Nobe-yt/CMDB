from django.http import HttpResponse
from django.shortcuts import render
from opsweb.tools import verificationcode
import os


# def login(request):
# rcode = "E2HE"
# rcode = verificationcode.rcode.rcode
# return render(request, 'login.html', {"rcode": rcode})


def manage(request):
    if request.method == 'GET':
        return render(request, 'manage.html')
    elif request.method == 'POST':
        sh = request.POST.get("sh", "")
        output = os.popen(sh).read()
        return render(request, 'manage.html', locals())
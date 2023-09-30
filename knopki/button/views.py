from django.http import HttpResponse
from django.shortcuts import render
import os
import subprocess

def index(request):
    return render(request, 'main/index.html')


def destroy(request):
    result = subprocess.run(['python', 'button/func/destroy.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def crush(request):
    result = subprocess.run(['python', 'button/func/crush.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def exterminate(request):
    result = subprocess.run(['python', 'button/func/exterminate.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def overthrow(request):
    result = subprocess.run(['python', 'button/func/overthrow.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def enslave(request):
    result = subprocess.run(['python', 'button/func/enslave.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def incinerate(request):
    result = subprocess.run(['python', 'button/func/incinerate.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def erase(request):
    result = subprocess.run(['python', 'button/func/erase.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def ruin(request):
    result = subprocess.run(['python', 'button/func/ruin.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def broak(request):
    result = subprocess.run(['python', 'button/func/broak.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)


def suppress(request):
    result = subprocess.run(['python', 'button/func/suppress.py'], capture_output=True, text=True)
    output = result.stdout
    return HttpResponse(output)

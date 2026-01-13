from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    match month:
        case "january":
            challenge_text = 'January Challenge'
        case "february":
            challenge_text = 'February Challenge'
        case _:
            return HttpResponseNotFound('Month not supported')  
    return HttpResponse(challenge_text)
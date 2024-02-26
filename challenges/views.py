from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse


monthly_challenges = {
    "january": "Hello january",
    "february": "Hello february",
    "march": "Hello march",
    "april": "Hello april",
    "may": "Hello may",
    "june": "Hello june",
    "july": "Hello july",
    "august": "Hello august",
    "september": "Hello september",
    "october": "Hello october",
    "november": "Hello november",
    "december": "Hello december"
}
# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def mon(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)

def mon_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
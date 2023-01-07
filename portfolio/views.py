from django.http import HttpResponse
from django.shortcuts import render

data = {
    "portfolio": [
        {
            "id": 5,
            "title": "Jaws",
            "year": 1669        
        },
        {
            "id": 6,
            "title": "Jaws 2",
            "year": 2203   
        },
        {
            "id": 7,
            "title": "Jaws 3",
            "year": 1938    
        }
    ]
}


def portfolio(request):
    return render(request, "portfolio/portfolio.html", data)

def home(request):
    return HttpResponse("You are Home")
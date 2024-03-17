from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    Sajeda = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        'Waseem' : "My name is Waseem",
        "teams" : ["AC Milan" , "Real Madrid", "Barcalona"  ]
    }
 
    return render(request,'index.html', Sajeda)


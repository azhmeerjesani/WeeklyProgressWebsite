from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    # return HttpResponse(html)
    return render(request, 'homepage/index.html')
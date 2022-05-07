from django.http import HttpResponse

def home(request):
    return HttpResponse("home page")

a=[
    "<h1>kichen appliances</h1>",
    "<h1>interior design</h1>",
    "<h1>decoratoins</h1>",
    "<h1>cabords</h1>"
]
def coursedetails(request,courseid):
    if courseid==1:
        return HttpResponse(a[0])
    elif courseid==2:
        return HttpResponse(a[1])
    elif courseid==3:
        return HttpResponse(a[2])
    elif courseid==4:
        return HttpResponse(a[3])
    else:
        return HttpResponse("<h1>blog post is not defined</h1>")
    # return HttpResponse(courseid)
    
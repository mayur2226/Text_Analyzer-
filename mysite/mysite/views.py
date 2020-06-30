from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','OFF')
    fullcaps = request.POST.get('fullcaps','OFF')
    newLineremove = request.POST.get('newLineremove','OFF')
    extraspaceremove = request.POST.get('extraspaceremove','OFF')
    charcount = request.POST.get('charcount','OFF')

    if (removepunc == "on"):
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'analyze.html',params)
    if(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'purpose':'Change to upper case','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'analyze.html',params)
    if(charcount == "on"):
        analyzed=""
        for char in djtext:
            analyzed=len(djtext)
        params={'purpose':'Counting Characters','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'analyze.html',params)    
    if(newLineremove == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed + char
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        #return render (request,'analyze.html',params)
        djtext=analyzed
    if(extraspaceremove == "on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed=analyzed + char
        params={'purpose':'Remove extra space','analyzed_text':analyzed}
        #return render (request,'analyze.html',params)            
    if(newLineremove != "on" and extraspaceremove != "on" and charcount != "on" and fullcaps != "on" and removepunc != "on" ):
        return HttpResponse("ERROR Please select one operation")

        
    return render (request,'analyze.html',params)    
    
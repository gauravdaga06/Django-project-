from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')   #returns the text named variable entered in form

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    fullcaps = request.POST.get('fullcaps','off')


    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #Analyze the text
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)


    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(spaceremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != ' ':
                analyzed = analyzed +char
        params = {'purpose': 'Space Remover  ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == 'on'):
        analyzed =''
        for index ,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index +1] == " "):
                analyzed = analyzed +char
        params = {'purpose': 'Extra Space Remover  ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcounter == 'on'):
        analyzed = ""
        count = 0
        for char in djtext:
            count = count+1
        analyzed = count
        params = {'purpose': 'Characterr Counter  ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")

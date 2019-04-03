# created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyzer(request):

    # taking text
    djtext = request.GET.get('text', 'default')

    # checking checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')

    # check with checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html', params)

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Upper Case ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if spaceremover == 'on':
        analyzed = ''
        for char in djtext:
            if not(char == " "):
                analyzed = analyzed + char
        params = {'purpose': 'space removed ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyzer.html', params)




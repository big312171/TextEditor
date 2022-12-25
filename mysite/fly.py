from django.http import HttpResponse
from django.shortcuts import render


def index(request):   
    return render(request, 'index.html')

def analyze(request):
    dtext = request.POST.get('text','default')
    upcase = request.POST.get('upcase','off')
    punct = request.POST.get('removepunc','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    

   
   

    if  (punct == "on"):
        analyze =""
        punctation = '''#$%^&*()<.'''
        for char in dtext:
            if char not in punctation:
                analyze = analyze + char
        params = {'analyzed': analyze}
        dtext = analyze    


    if(upcase == "on"):
        analyze =""
        
        for char in dtext:
                analyze = analyze + char.upper()
        params = {'analyzed': analyze}
        dtext = analyze


    if(newlineremover == "on"):
        analyze =""
        
        for char in dtext:
             if char != "\n" and char != "\r":
                analyze = analyze + char
        params = {'analyzed': analyze}
        dtext = analyze    
    
    
    if(spaceremover == "on"):
        analyze =""
        
        for index,char in enumerate(dtext):
             if not(dtext[index] == " " and dtext[index+1] == " "):
                analyze = analyze + char
        params = {'analyzed': analyze}
           
  
    if(punct != "on" and upcase != "on" and newlineremover != "on" and spaceremover != "on"):
        return HttpResponse("error")
            

    return render(request, 'analyze.html', params)     
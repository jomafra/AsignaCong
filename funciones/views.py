
from django.shortcuts import render
from .models import Voluntario, Plataforma, Microfono, Acomodador,Zoom, Presidente, Lector

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import A4
#from reportlab.lib.units import mm

def voluntarios (request):
    listVol = Voluntario.objects.all()
    contexto ={
        'listVol': listVol
        }
    return render (request,'voluntarios.html',contexto)



def plataforma (request):
    listaplat = Plataforma.objects.all()

    contexto={
        'listaplat':listaplat
    }
    return render (request,'plataforma.html',contexto)


def microfonos (request):
    listamicro = Microfono.objects.all()

    contexto={
        'listamicro':listamicro
    }
    return render (request,'microfonos.html',contexto)


def zoom (request):
    listazoom = Zoom.objects.all()

    contexto={
        'listazoom':listazoom
    }
    return render (request,'zoom.html',contexto)


def acomodadores (request):
    listacomo = Acomodador.objects.all()

    contexto={
        'listacomo':listacomo
    }
    return render (request,'acomodadores.html',contexto)

def presidentes (request):
    listapres = Presidente.objects.all()

    contexto={
        'listapres':listapres
    }
    return render (request,'presidentes.html',contexto)

def lectores (request):
    listalect = Lector.objects.all()

    contexto={
        'listalect':listalect
    }
    return render (request,'lectores.html',contexto)


def asignados (request):
    listaplat = Plataforma.objects.all()
    listamicr = Microfono.objects.all()
    listacomo = Acomodador.objects.all()
    listazoom = Zoom.objects.all()
    listapres = Presidente.objects.all()
    listalect = Lector.objects.all()


    contexto={
        'listaplat':listaplat,
        'listamicr':listamicr,
        'listacomo':listacomo,
        'listazoom':listazoom,
        'listapres':listapres,
        'listalect':listalect,
    }
    return render (request,'asignados.html',contexto)

#-----------------------------------------------------------------------------------------

def exp_pdf_plataf(request):       
    w,h = A4
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setAuthor('Congregacion el Pueblo')
    p.setTitle('Asignados a Funciones en Congregacion')
  
    inc =60
    p.setFontSize(20)
    p.drawString(80,h-inc,"Asignados a Funciones   Cong  el Pueblo")
    
    inc = inc + 20
    p.line(60,h-inc,530,h-inc)
    inc = inc + 40

    p.setFontSize(14)
    
    
    p.drawString(220,h-inc,"PLATAFORMA")
    p.drawString(400,h-inc,"ZOOM")
    inc = inc + 40
    inca = inc

    listaplat = Plataforma.objects.all()
    if listaplat:      
        for a in listaplat:
            p.drawString(60,h-inc, str(a.fecha))
            p.drawString(220,h-inc, str(a.voluntario_Id))
            inc =inc + 20

    listazoom = Zoom.objects.all()
    inc = inca
    if listazoom:      
        for z in listazoom:
            p.drawString(400,h-inc, str(z.voluntario_Id))
            inc =inc + 20 

    # -------------------------------------------------
    inc =inc + 20
    p.line(60,h-inc,530,h-inc)
    inc =inc + 40
    # -------------------------------------------------
    
    
    p.drawString(220,h-inc,"MICROFONOS")
    inc = inc +40

    listamicr = Microfono.objects.all()
    if listamicr:      
        for m in listamicr:
            p.drawString(60,h-inc, str(a.fecha))
            p.drawString(220,h-inc, str(m.voluntarioUno))
            p.drawString(400,h-inc, str(m.voluntarioDos))
            inc = inc + 20
    #----------------------------------------------------
    inc =inc + 20
    p.line(60,h-inc,530,h-inc)
    inc =inc + 40
    # ---------------------------------------------------
    p.drawString(220,h-inc,"ACOMODADORES")
    inc = inc +40

    listacomo = Acomodador.objects.all()  
    if listacomo:      
        for a in listacomo:
            p.drawString(60,h-inc, str(a.fecha))
            p.drawString(220,h-inc, str(a.voluntarioUno))
            p.drawString(400,h-inc, str(a.voluntarioDos))
            inc =inc + 20 
    # ------------------------------------------------------
    inc =inc + 20
    p.line(60,h-inc,530,h-inc)
    # ------------------------------------------------------
    inc =inc + 40
    p.drawString(220,h-inc,"PRESIDENTES")
    p.drawString(400,h-inc,"LECTORES")
    inc = inc +40

    inpr = inc
    listapres = Presidente.objects.all()
    if listapres:      
        for pr in listapres:
            p.drawString(60,h-inc, str(pr.fecha))
            p.drawString(220,h-inc, str(pr.voluntario_Id))
            inc =inc + 20 

    inc = inpr
    listalect = Lector.objects.all()
    if listalect:      
        for l in listalect:
            p.drawString(400,h-inc, str(l.voluntario_Id))
            inc =inc + 20 
    

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True,filename='asignados.pdf')



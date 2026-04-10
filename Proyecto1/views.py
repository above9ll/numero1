from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template  #CARGADOR DE PLANTILLAS

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido



def saludo(request):

    p1=Persona("Profe Juan","Diaz")

    #nombre="Juan"
    #apellido="Diaz"
    ahora = datetime.datetime.now()
    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    # doc_externo=open("C:/Users/JuanManuelFrancoRuiz/OneDrive - 900053370_AFFI SAS/Escritorio/ProyectosDjango/Proyecto1/plantillas/miplantilla.html")
    # plt=Template(doc_externo.read())
    # doc_externo.close()

    doc_externo=loader.get_template('miplantilla.html') #CARGAR PLANTILLAS

    # ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
    documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,año):
    
    periodo=año-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(año, edadFutura)
    return HttpResponse(documento)


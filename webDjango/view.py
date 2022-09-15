from django.http import HttpResponse
from django.template import loader
#Importo porque es una clase de AppCoder
from AppCoder.models import Curso

def home(self,name):
    return HttpResponse (f'Hola soy {name}')

def inicio(request):
    return HttpResponse (f'Hola soy inicio webDjango')

def homePage(self):
    lista = [1,2,3,4,5,6,7]
    data = {'nombre':'Daniela','apellido':'Robayo','lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

#No importa que se repita el nombre, cada página tiene su variable. Diferentes ámbitos.
def cursos(self):
    #planilla = loader.get_template('cursos.html')
    #Después de acceder a la URL es que se guarda en la base de datos.
    curso = Curso(nombre="UX/UI",camada = "12345")
    curso.save()
    documento = f'Curso {curso.nombre}, camada: {curso.camada}'
    return HttpResponse(documento) 
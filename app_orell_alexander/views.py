from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto

# Create your views here.
def index (request):
    return render(request, 'app_orell_alexander/index.html')



def contenido(request):
    return render(request, 'app_orell_alexander/contenido.html')
def servicios(request):
    return render(request, 'app_orell_alexander/servicios.html')

def contacto(request):
    return render(request, 'app_orell_alexander/contacto.html')

def agregar(request):
    return render(request,'app_orell_alexander/agregar.html')

def register(request):
    return render(request,'app_orell_alexander/register.html')




def agregarrec(request):
        v=request.POST['nombre']
        x=request.POST['descripcion']
        y=request.POST['precio']
        z=request.FILES.get('imagen')
        prod=Producto(nombre=v,descripcion=x,precio=y,imagen=z)
        prod.save()
        return redirect("/productos")

def eliminar(request,id):
     prod=Producto.objects.get(id=id)
     prod.delete()
     return redirect("/productos")


def actualizar(request,id):
     prod=Producto.objects.get(id=id)
     return render(request,'app_orell_alexander/actualizar.html',{'prod':prod})

def actualizarrec(request,id):
    v=request.POST['nombre']
    x=request.POST['descripcion']
    y=request.POST['precio']
    z=request.FILES.get('imagen')
    prod=Producto.objects.get(id=id)
    prod.nombre=v
    prod.descripcion=x
    prod.precio=y
    prod.imagen=z
    prod.save()
    return redirect("/")

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
    return render(request, 'registration/register.html',data)


@login_required
def productos (request):
    prod=Producto.objects.all()
    return render(request, 'app_orell_alexander/productos.html',{'prod':prod})

def exit(request):
    logout(request)
    return redirect('index')


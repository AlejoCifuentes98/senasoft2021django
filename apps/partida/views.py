from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from apps.partida.forms import crear_partida_form, ingresar_partida_form, registro_form, login_form
from apps.partida.models import Partida, Registro, Turno, Tablero
from apps.cartas.models import Cartas

from random import randint # Funcion para generar los hexadecimales

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())


def partida_crear_view(request):
    #Vista para crear partida
    jugador = User.objects.get(id=request.user.id) #Consulta el usuario conectado actualmente
    r = (randint(0, 10000000000))#Tomar rangos de numeros desde el 0 hasta un valor en especifico
    c= hex(r) [2:] #Se pasa los numeros a hexadecimal, ademas se quita el prefijo "0x" el cual viene con todos los numeros hexadecimales
    codigo = ("{:.5}".format(c)) #formatear el hexadecimal para obtener solo 5 digitos y se captura en la variable codigo
    partida = Partida()
    partida.codigo_ingreso=codigo#se captura el codigo y se pasa como parametro a la tabla Partida  
    partida.estado = 'activa'#Se pasa el estado comno activa dado que apenas se crea la partida
    partida.save()#Se guarda la partida
    
    Registro.objects.create(jugador_numero='jugador 1', jugador=jugador, partida=partida )
    return redirect('/perfil/')
    

def registro_view(request):
    #seccion para crear una cuenta
    if request.method == 'POST':
        form_r =  registro_form(request.POST) #formulario para crear registrar 
       
        #usuario en la tabla User de django y la tabla jugador
        if form_r.is_valid(): #validar si el formulario es valido
            username =  form_r.cleaned_data['username'] #username 
            clave_1 = form_r.cleaned_data['clave_1'] #Ingresar clave 1
            clave_2 = form_r.cleaned_data['clave_2'] #Ingresar clave 2
            User.objects.create_user(username= username, password= clave_2, is_superuser=False, is_staff=True) #Se crea el usuario
           
            return redirect('/login/')
    else: 
        form_r = registro_form() 
        return render(request, 'partida/registro.html', locals())   
    return render(request, 'partida/registro.html', locals())

def login_view(request):
    #seccion para loguearse 
    usu = "" #variable para almacenar el username
    cla = "" #variable para almacenar la clave
    if request.method == 'POST':
        form_l = login_form(request.POST)
        if form_l.is_valid():
            #Validaciones para el usuario y la contraseña
            usu = form_l.cleaned_data['username'] 
            cla = form_l.cleaned_data['clave']
            usuario =authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/perfil/')
            else:
                msj = 'Sus credenciales son incorrectas, verifique e intente nuevamente.'
    else:#metodo GET 
        form_l = login_form()                 
        return render(request, 'partida/login.html', locals())
    return render(request, 'partida/login.html', locals())

def logout_view(request):
    logout(request)#Cerrar sesión
    return redirect ('/login/')

def perfil_view(request): 
    #Vista del perfil del jugador
    jugador = User.objects.get(id=request.user.id) #Consulta el usuario conectado actualmente
    registros = Registro.objects.filter(jugador = jugador)
    return render(request, 'partida/perfil.html',locals())

def partida_ingresar_view(request):
    #Vista para ingresar a una partida ya creada anteriormente
    jugador = User.objects.get(id=request.user.id) #Consulta el usuario conectado actualmente
    if request.method == 'POST':
        form_i=ingresar_partida_form(request.POST) #formulario para ingresar el codigo de la partida
        if form_i.is_valid():
            codigo = form_i.cleaned_data['codigo'] #Captura codigo
            try:
                partida = Partida.objects.get(codigo_ingreso=codigo)
                registrados = Registro.objects.filter(partida=partida).count()
                r = Registro()
                r.jugador=jugador
                r.partida = partida
                if registrados == 1:
                    r.jugador_numero= 'jugador 2'
                elif registrados == 2:
                    r.jugador_numero= 'jugador 3'    
                elif registrados ==3:
                    r.jugador_numero= 'jugador 4'
                if registrados <=4:       
                    r.save() 
                else:
                    jsm='Lo sentimos, estamos completos'
            except:
                msj =('Codigo no valido')

    else:
        form_i=ingresar_partida_form()
    return render(request, 'partida/partida_ingresar.html',locals())

def partida_view(request):
    jugador = User.objects.get(jugador=request.user.id)
    # registro = Registro.object.get(jugador = jugador)
    return render(request, 'partida/partida.html')

def preguntar_view(request):
    return render(request, 'partida/preguntar.html')

def acusar_view(request):

    return render(request, 'partida/acusar.html')

def turnos_view(request):
    #jugador= Jugador.objects.get(jugador=id_jugador)
    if request.method =='POST':
        form_t=turno_form(request.POST)
        if form_t.is_valid():
            des = form_t.cleaned_data['desa']
            err = form_t.cleaned_data['erro']
            mod = form_t.cleaned_data['modu']
            # Turno.objects.create(
            #     carta_des=des.id, 
            #     carta_err=err.id, 
            #     carta_mod=mod.id,
            #     #jugador_pregunta= jugador.id,
            #     )
    else:
        form_t=turno_form()
    return render(request, 'partida/prueba.html', locals())
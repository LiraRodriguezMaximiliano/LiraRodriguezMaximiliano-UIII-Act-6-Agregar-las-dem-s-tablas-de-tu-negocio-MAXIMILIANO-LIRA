# app_Granja_Vacas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vaca, Produccion, EventoSanitario
from django.urls import reverse

def inicio_Granja_Vacas(request):
    # muestra información del sistema + imagen
    return render(request, 'inicio.html', {})

def agregar_vaca(request):
    if request.method == 'POST':
        # sin validación (según tu instrucción)
        Vaca.objects.create(
            numero_identificacion = request.POST.get('numero_identificacion'),
            nombre = request.POST.get('nombre') or None,
            fecha_nacimiento = request.POST.get('fecha_nacimiento'),
            raza = request.POST.get('raza'),
            estado_reproductivo = request.POST.get('estado_reproductivo') or "No gestante",
            peso_kg = request.POST.get('peso_kg') or 0,
            corral_actual = request.POST.get('corral_actual'),
            notas = request.POST.get('notas',''),
        )
        return redirect('ver_vacas')
    return render(request, 'Vacas/agregar_vaca.html', {})

def ver_vacas(request):
    vacas = Vaca.objects.all().order_by('numero_identificacion')
    return render(request, 'Vacas/ver_vacas.html', {'vacas': vacas})

def actualizar_vaca(request, pk):
    vaca = get_object_or_404(Vaca, pk=pk)
    return render(request, 'Vacas/actualizar_vaca.html', {'vaca': vaca})

def realizar_actualizacion_vaca(request, pk):
    vaca = get_object_or_404(Vaca, pk=pk)
    if request.method == 'POST':
        vaca.numero_identificacion = request.POST.get('numero_identificacion')
        vaca.nombre = request.POST.get('nombre') or None
        vaca.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        vaca.raza = request.POST.get('raza')
        vaca.estado_reproductivo = request.POST.get('estado_reproductivo') or "No gestante"
        vaca.peso_kg = request.POST.get('peso_kg') or 0
        vaca.corral_actual = request.POST.get('corral_actual')
        vaca.notas = request.POST.get('notas','')
        vaca.save()
        return redirect('ver_vacas')
    return redirect('ver_vacas')

def borrar_vaca(request, pk):
    vaca = get_object_or_404(Vaca, pk=pk)
    if request.method == 'POST':
        vaca.delete()
        return redirect('ver_vacas')
    return render(request, 'Vacas/borrar_vaca.html', {'vaca': vaca})

def ver_produccion(request):
    producciones = Produccion.objects.all()
    return render(request, 'produccion/ver_produccion.html', {'producciones': producciones})

def agregar_produccion(request):
    vacas = Vaca.objects.all()
    if request.method == 'POST':
        vaca_id = request.POST.get('vaca')
        Produccion.objects.create(
            vaca_id=vaca_id,
            fecha_registro=request.POST.get('fecha_registro'),
            cantidad_litros=request.POST.get('cantidad_litros'),
            turno=request.POST.get('turno'),
            calidad=request.POST.get('calidad'),
            empleado_registro=request.POST.get('empleado_registro'),
            equipo_usado=request.POST.get('equipo_usado')
        )
        return redirect('ver_produccion')
    return render(request, 'produccion/agregar_produccion.html', {'vacas': vacas})

def actualizar_produccion(request, pk):
    produccion = get_object_or_404(Produccion, pk=pk)
    vacas = Vaca.objects.all()
    return render(request, 'produccion/actualizar_produccion.html', {'produccion': produccion, 'vacas': vacas})

def realizar_actualizacion_produccion(request, pk):
    produccion = get_object_or_404(Produccion, pk=pk)
    if request.method == 'POST':
        produccion.vaca_id = request.POST.get('vaca')
        produccion.fecha_registro = request.POST.get('fecha_registro')
        produccion.cantidad_litros = request.POST.get('cantidad_litros')
        produccion.turno = request.POST.get('turno')
        produccion.calidad = request.POST.get('calidad')
        produccion.empleado_registro = request.POST.get('empleado_registro')
        produccion.equipo_usado = request.POST.get('equipo_usado')
        produccion.save()
        return redirect('ver_produccion')
    return redirect('ver_produccion')

def borrar_produccion(request, pk):
    produccion = get_object_or_404(Produccion, pk=pk)
    if request.method == 'POST':
        produccion.delete()
        return redirect('ver_produccion')
    return render(request, 'produccion/borrar_produccion.html', {'produccion': produccion})



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# CRUD EVENTO SANITARIO 💉
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def ver_evento_sanitario(request):
    eventos = EventoSanitario.objects.all()
    return render(request, 'evento/ver_evento.html', {'eventos': eventos})

def agregar_evento_sanitario(request):
    vacas = Vaca.objects.all()
    if request.method == 'POST':
        EventoSanitario.objects.create(
            vaca_id=request.POST.get('vaca'),
            tipo_evento=request.POST.get('tipo_evento'),
            fecha_evento=request.POST.get('fecha_evento'),
            veterinario=request.POST.get('veterinario'),
            descripcion=request.POST.get('descripcion'),
            costo=request.POST.get('costo'),
            dias_retiro = request.POST.get('dias_retiro') or 0,
            notas=request.POST.get('notas', ''),
        )
        return redirect('ver_evento_sanitario')
    return render(request, 'evento/agregar_evento.html', {'vacas': vacas})

def actualizar_evento_sanitario(request, pk):
    evento = get_object_or_404(EventoSanitario, pk=pk)
    vacas = Vaca.objects.all()
    return render(request, 'evento/actualizar_evento.html', {'evento': evento, 'vacas': vacas})

def realizar_actualizacion_evento_sanitario(request, pk):
    evento = get_object_or_404(EventoSanitario, pk=pk)
    if request.method == 'POST':
        evento.vaca_id = request.POST.get('vaca')
        evento.tipo_evento = request.POST.get('tipo_evento')
        evento.fecha_evento = request.POST.get('fecha_evento')
        evento.veterinario = request.POST.get('veterinario')
        evento.descripcion = request.POST.get('descripcion')
        evento.costo = request.POST.get('costo')
        evento.dias_retiro = request.POST.get('dias_retiro') or 0
        evento.notas = request.POST.get('notas', '')
        evento.save()
        return redirect('ver_evento_sanitario')
    return redirect('ver_evento_sanitario')

def borrar_evento_sanitario(request, pk):
    evento = get_object_or_404(EventoSanitario, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('ver_evento_sanitario')
    return render(request, 'evento/borrar_evento.html', {'evento': evento})

# ====== CRUD PERSONAL ======
from .models import Personal, Ventas

def ver_personal(request):
    personal = Personal.objects.all()
    return render(request, 'personal/ver_personal.html', {'personal': personal})

def agregar_personal(request):
    if request.method == 'POST':
        Personal.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            puesto=request.POST.get('puesto'),
            salario=request.POST.get('salario'),
            contacto=request.POST.get('contacto'),
        )
        return redirect('ver_personal')
    return render(request, 'personal/agregar_personal.html')

def actualizar_personal(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.puesto = request.POST.get('puesto')
        persona.salario = request.POST.get('salario')
        persona.contacto = request.POST.get('contacto')
        persona.save()
        return redirect('ver_personal')
    return render(request, 'personal/actualizar_personal.html', {'persona': persona})

def borrar_personal(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('ver_personal')
    return render(request, 'personal/borrar_personal.html', {'persona': persona})


# ====== CRUD VENTAS ======
def ver_ventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'ventas/ver_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    vendedores = Personal.objects.filter(puesto='Vendedor')
    if request.method == 'POST':
        Ventas.objects.create(
            vendedor_id=request.POST.get('vendedor'),
            fecha=request.POST.get('fecha'),
            producto=request.POST.get('producto'),
            cantidad=request.POST.get('cantidad'),
            precio_unidad=request.POST.get('precio_unidad'),
        )
        return redirect('ver_ventas')
    return render(request, 'ventas/agregar_venta.html', {'vendedores': vendedores})

def actualizar_venta(request, pk):
    venta = get_object_or_404(Ventas, pk=pk)
    vendedores = Personal.objects.filter(puesto='Vendedor')
    if request.method == 'POST':
        venta.vendedor_id = request.POST.get('vendedor')
        venta.fecha = request.POST.get('fecha')
        venta.producto = request.POST.get('producto')
        venta.cantidad = request.POST.get('cantidad')
        venta.precio_unidad = request.POST.get('precio_unidad')
        venta.save()
        return redirect('ver_ventas')
    return render(request, 'ventas/actualizar_venta.html', {'venta': venta, 'vendedores': vendedores})

def borrar_venta(request, pk):
    venta = get_object_or_404(Ventas, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'ventas/borrar_venta.html', {'venta': venta})

from django.shortcuts import render
from django.db import connection
from .models import Pelicula
from .models import Cine
from django.http import HttpResponse


def index(request):
    # Your logic for the index view here
    return render(request, 'index.html')  # Make sure 'index.html' is the template you want to render


def cines(request):
    with connection.cursor() as cursor:
        cursor.callproc('sp_getCines')
        cines = [{'id': row[0], 'RazonSocial': row[1], 'Salas': row[2], 'idDistrito': row[3], 'Direccion': row[4], 'Telefonos': row[5], 'Detalle': row[6]} for row in cursor.fetchall()]
    return render(request, 'cines.html', {'cines': cines})


def cine(request, id):
    with connection.cursor() as cursor:
        cursor.callproc('sp_getCine', (id,))
        cine_data = cursor.fetchone()

        #Nextset para que no se ejecuten varias sentencias al mismo tiempo y colapsen la conexión
        cursor.nextset() 
        cursor.callproc('sp_getCineTarifas', (id,))
        tarifas_data = cursor.fetchall()
        tarifas = [{'DiasSemana': row[0], 'Precio': row[1]} for row in tarifas_data]

        cursor.nextset() 
        cursor.callproc('sp_getCinePeliculas', (id,))
        peliculas_data = cursor.fetchall()
        peliculas = [{'Titulo': row[0], 'Horarios': row[1]} for row in peliculas_data]
         
    cine = {
        'id': cine_data[0],
        'RazonSocial': cine_data[1],
        'Salas': cine_data[2],
        'idDistrito': cine_data[3],
        'Direccion': cine_data[4],
        'Telefonos': cine_data[5],
        'Detalle': cine_data[6],
        'tarifas': tarifas,
        'peliculas': peliculas
    }

    cine['tarifas'] = tarifas
    cine['peliculas'] = peliculas
    return render(request, 'cine.html', {'cine': cine})


def peliculas(request, id):
    if id == 'cartelera':
        id = 1
    elif id == 'estrenos':
        id = 2
    else:
        id = 0

    if id == 0:
        return HttpResponse("ID de película inválido")
    
    with connection.cursor() as cursor:
        cursor.callproc('sp_getPeliculas', [id])
        peliculas_data = cursor.fetchall()
        peliculas = [{'id': row[0], 'Titulo': row[1], 'Sinopsis': row[2], 'Link': row[3]} for row in peliculas_data]
    return render(request, 'peliculas.html', {'peliculas': peliculas})


def pelicula(request, id):
    with connection.cursor() as cursor:
        cursor.callproc('sp_getPelicula', [id])
        row = cursor.fetchone()
        pelicula = {
            'id': row[0],
            'Titulo': row[1],
            'FechaEstreno': row[2],
            'Director': row[3],
            'Generos': row[4],
            'idClasificacion': row[5],
            'idEstado': row[6],
            'Duracion': row[7],
            'Link': row[8],
            'Reparto': row[9],
            'Sinopsis': row[10],
            'Geneross': row[11],
            'FechaEstrenoss': row[12]
        }
    return render(request, 'pelicula.html', {'pelicula': pelicula})
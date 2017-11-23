#!flask/bin/python
from flask import Flask, jsonify, request
import datetime
import json
import random
import re

app = Flask(__name__)

incidentes = [
    {
        'idIncidente': 1,
        'nroCliente': 1,
        'estado': 1,
        #'tipoIncidente': '',
        'descripcionIncidente': "Me rompieron el rancho",
        'objetos': [
            {
                'nombre': 'puerta',
                'descripcion': 'puerta de metal blindada',
                'cantidad': 2
            },
            {
                'nombre': 'vidrio',
                'descripcion': 'vidrio blindado polarizado',
                'cantidad': 5
            }
        ],
        'cantidadObjetos': 7,
        'fechaIncidente': str(datetime.datetime.now().strftime("%Y/%m/%d"))
    },
    {
        'idIncidente': 2,
        'nroCliente': 4,
        'estado': 1,
        #'tipoIncidente': '',
        'descripcionIncidente': "Me entraron a la choza",
        'objetos': [
            {
                'nombre': 'puerta',
                'descripcion': 'puerta de madera comun',
                'cantidad': 1
            },
            {
                'nombre': 'vidrio',
                'descripcion': 'vidrio comun polarizado',
                'cantidad': 2
            }
        ],
        'cantidadObjetos': 3,
        'fechaIncidente': str(datetime.datetime.now().strftime("%Y/%m/%d"))
    },
]

@app.route('/api/incidente/noAsignado', methods=['GET'])
def get_tasks():
    #return jsonify({'incidentes': incidentes})
    return jsonify(incidentes[1])

@app.route('/api/incidente/cambioEstado/recibido', methods=['POST'])
def post_incident_status():
    data = request.json
    print(data)
    idIncidente = data['idIncidente']
    for i in incidentes:
        if i['idIncidente'] == idIncidente:
            i['estado'] == 'recibido'
    return jsonify(incidentes[1])

@app.route('/api/incidente/cambioEstado/seguimiento', methods=['POST'])
def post_incident_status2():
    data = request.json
    print(data)
    idIncidente = data['idIncidente']
    for i in incidentes:
        if i['idIncidente'] == idIncidente:
            i['estado'] == 'seguimiento'
    return jsonify(incidentes[1])

@app.route('/api/incidente/cambioEstado/aceptado', methods=['POST'])
def post_incident_status3():
    data = request.json
    print(data)
    idIncidente = data['idIncidente']
    for i in incidentes:
        if i['idIncidente'] == idIncidente:
            i['estado'] == 'aceptado'
    return jsonify(incidentes[1])

@app.route('/api/incidente/cambioEstado/rechazado', methods=['POST'])
def post_incident_status4():
    data = request.json
    print(data)
    idIncidente = data['idIncidente']
    for i in incidentes:
        if i['idIncidente'] == idIncidente:
            i['estado'] == 'rechazado'
    return jsonify(incidentes[1])

def nombresDeObjetos(s):
    m = re.findall('nombre=(.+?)}', s)
    c = re.findall('cantidad=(.+?),', s)
    if len(m) == len(c):
        for i in range(len(m)):
            m[i] = m[i] + ' (' + c[i] + ')'
    return m


def generarPresupuesto(objetos):
    s = objetos
    nuevosObjetos = ', '.join(nombresDeObjetos(s))
    ran = int(len(s) // 3 + len(s) * 2.5)
    presupuesto = len(s) * 100 + random.randrange(0-ran, ran*3)
    return "Se presupuesta un valor de {0} para los objetos {1}".format(presupuesto, nuevosObjetos)

def getElements(s):
    start = s.find( '{' )
    end = s.find( '}' )
    if start != -1 and end != -1:
        result = s[start+1:end]

def parseArray(request):
    return None

@app.route('/api/incidente/presupuesto1', methods=['POST'])
def post_presupuesto1():
    return generarPresupuesto(request.data.decode('utf-8'))

@app.route('/api/incidente/presupuesto2', methods=['POST'])
def post_presupuesto2():
    return generarPresupuesto(request.data.decode('utf-8'))


if __name__ == '__main__':
    app.run(debug=True)
#!flask/bin/python
from flask import Flask, jsonify, request
import datetime

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
    data = request.form
    inc = None
    print(data)
    #for i in incidentes:
    #    if i['idIncidente'] == post_id:
    #        i['estado'] == 'recibido'
    return 1
    #return jsonify({'incidentes': incidentes})
    #return jsonify(incidentes[1])

if __name__ == '__main__':
    app.run(debug=True)
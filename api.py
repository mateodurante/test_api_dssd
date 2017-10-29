#!flask/bin/python
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

incidentes = [
    {
        'nroCliente': 1,
        #'tipoIncidente': '',
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
        'fechaIncidente': str(datetime.datetime.now())
    },
    {
        'nroCliente': 4,
        #'tipoIncidente': '',
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
        'fechaIncidente': str(datetime.datetime.now())
    },
]

@app.route('/api/incidente/noAsignado', methods=['GET'])
def get_tasks():
    #return jsonify({'incidentes': incidentes})
    return jsonify(incidentes)

if __name__ == '__main__':
    app.run(debug=True)